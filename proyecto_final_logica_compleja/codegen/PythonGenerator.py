class PythonCodeGenerator:
    def __init__(self):
        self.tac = []
        self.labels = {}
        self.if_regions = {}
        self.while_regions = {}
        self.func_regions = {}
        self.func_names = set()
        self.call_args_buffer = []


    def generate_from_tac(self, tac):
        self.tac = list(tac)
        self.labels = {
            inst['op'][:-1]: i
            for i, inst in enumerate(self.tac)
            if isinstance(inst.get('op'), str) and inst['op'].endswith(':')
        }
        self._detect_functions()
        self._detect_while_regions()
        self._detect_if_regions()
        expr = self._build_expr_map()

        out = []
        def E(s, ind=0): out.append(("    " * ind) + s)

        # helpers booleanos
        E("def nand(x, y):"); E("return not (x and y)", 1)
        E("def nor(x, y):");  E("return not (x or y)", 1)
        E("def xnor(x, y):"); E("return x == y", 1)
        E("")


        need_preinit = self._preinit_needed_for_range(expr, 0, len(self.tac), only_module=True)
        for v in need_preinit:
            E(f"{v} = False")
        if need_preinit:
            E("")

        i = 0
        n = len(self.tac)
        self.call_args_buffer = []
        while i < n:
            if i in self.func_regions:
                i = self._emit_function(i, expr, E); continue
            if i in self.if_regions:
                i = self._emit_if_block(i, expr, E, base=0,
                                        loop_start_label=None, loop_end_label=None); continue
            if i in self.while_regions:
                i = self._emit_while_block(i, expr, E, base=0); continue

            inst = self.tac[i]
            op = inst.get('op')
            if isinstance(op, str) and op.endswith(':'):
                i += 1; continue

            if op == 'PARAM':
                self.call_args_buffer.append(self._render_expr(inst['arg1'], expr))
            elif op == 'CALL':
                fn = inst['arg1']; args = ", ".join(self.call_args_buffer); self.call_args_buffer.clear()
                if inst.get('result'): E(f"{inst['result']} = {fn}({args})", 0)
                else:                   E(f"{fn}({args})", 0)
            elif op == 'RETURN':
                if inst.get('arg1') is None: E("return", 0)
                else:                        E(f"return {self._render_expr(inst['arg1'], expr)}", 0)
            elif op == 'PRINT':
                E(f"print({self._render_expr(inst['arg1'], expr)})", 0)
            elif op == '=' and self._is_user(inst['result']):
                E(f"{inst['result']} = {self._render_expr(inst['arg1'], expr)}", 0)
            # 'goto' a nivel módulo se ignora
            i += 1

        return "\n".join(out)


    def _detect_functions(self):
        i = 0; n = len(self.tac)
        while i < n:
            op = self.tac[i].get('op')
            if isinstance(op, str) and op.startswith("FUNCTION "):
                name = op[len("FUNCTION "):].rstrip(':').strip()
                self.func_names.add(name)
                j = i + 1; end_idx = None
                while j < n:
                    opj = self.tac[j].get('op')
                    if isinstance(opj, str) and opj.startswith("END FUNCTION"):
                        end_idx = j; break
                    j += 1
                if end_idx is None: end_idx = n - 1
                self.func_regions[i] = (name, i, end_idx)
                i = end_idx + 1; continue
            i += 1

    def _detect_while_regions(self):
        i = 0; n = len(self.tac)
        while i < n:
            op = self.tac[i].get('op')
            if isinstance(op, str) and op.endswith(':'):
                start = i; j = i + 1
                while j < n and self.tac[j].get('op') != 'if_false_goto':
                    if isinstance(self.tac[j].get('op'), str) and self.tac[j]['op'].endswith(':'):
                        break
                    j += 1
                if j < n and self.tac[j].get('op') == 'if_false_goto':
                    end_label = self.tac[j]['result']
                    lend = self.labels.get(end_label, None)
                    if lend is not None:
                        k = lend - 1
                        while k > j and self.tac[k].get('op') != 'goto':
                            k -= 1
                        if k > j and self.tac[k]['result'] == self.tac[i]['op'][:-1]:
                            self.while_regions[i] = (i, j, k, lend)
                            i = lend + 1; continue
            i += 1

    def _detect_if_regions(self):
        i = 0; n = len(self.tac)
        while i < n:
            if self.tac[i].get('op') == 'if_false_goto':
                idx_else = self.labels.get(self.tac[i]['result'], None)
                if idx_else is None: i += 1; continue
                goto_end_idx = idx_else - 1 if idx_else - 1 >= 0 else None
                has_else = goto_end_idx is not None and self.tac[goto_end_idx].get('op') == 'goto'
                if has_else:
                    end_label = self.tac[goto_end_idx]['result']
                    lend = self.labels.get(end_label, None)
                    if lend is not None and lend > idx_else:
                        self.if_regions[i] = ('ifelse', i, idx_else, goto_end_idx, lend)
                        i = lend + 1; continue
                else:
                    self.if_regions[i] = ('ifonly', i, idx_else)
                    i = idx_else + 1; continue
            i += 1

    def _emit_function(self, i, expr, E):
        name, fstart, fend = self.func_regions[i]
        params, body_start = self._collect_func_params(fstart + 1, fend)
        sig = f"def {name}({', '.join(params)}):" if params else f"def {name}():"
        E(sig, 0)

        need_preinit = self._preinit_needed_for_range(expr, body_start, fend, only_module=False)
        if need_preinit:
            for v in need_preinit:
                if v not in params:
                    E(f"{v} = False", 1)

        self._emit_range(body_start, fend, expr, E, indent=1,
                         loop_start_label=None, loop_end_label=None)
        return fend + 1

    def _collect_func_params(self, start, end):
        params = []; idx = start
        while idx < end and isinstance(self.tac[idx].get('op'), str) and self.tac[idx]['op'].endswith(':'):
            idx += 1
        while idx < end and self.tac[idx].get('op') == 'PARAM_RECEIVE':
            pname = self.tac[idx].get('result')
            if isinstance(pname, str) and pname.isidentifier():
                params.append(pname)
            idx += 1
        return params, idx


    def _range_will_emit(self, start, end, loop_start_label, loop_end_label):
        """Devuelve True si esa región producirá alguna línea (break/continue o código real)."""
        i = start
        while i < end:
            op = self.tac[i].get('op')
            if isinstance(op, str) and op.endswith(':'):
                i += 1; continue
            if i in self.if_regions or i in self.while_regions:
                return True
            if op == 'goto':
                tgt = self.tac[i].get('result')
                if (loop_end_label and tgt == loop_end_label) or (loop_start_label and tgt == loop_start_label):
                    return True
            elif op in ('PARAM','CALL','RETURN','PRINT','='):
                return True
            i += 1
        return False


    def _emit_if_block(self, i, expr, E, base, loop_start_label, loop_end_label):
        info = self.if_regions[i]

        def empty(start, end):

            return not self._range_will_emit(start, end, loop_start_label, loop_end_label)


        if info[0] == 'ifonly':
            _, if_idx, idx_else = info
            cond = self._render_expr(self.tac[if_idx]['arg1'], expr)


            if loop_end_label and self._range_is_only_goto_to(if_idx + 1, idx_else, loop_end_label):
                E(f"if {cond}:", base)
                E("break", base + 1)
                return idx_else + 1


            if empty(if_idx + 1, idx_else):
                return idx_else + 1

            E(f"if {cond}:", base)
            self._emit_range(if_idx + 1, idx_else, expr, E, indent=base + 1,
                             loop_start_label=loop_start_label, loop_end_label=loop_end_label)
            return idx_else + 1

        # if-else
        else:
            _, if_idx, idx_else, goto_end_idx, lend = info
            cond = self._render_expr(self.tac[if_idx]['arg1'], expr)
            then_start, then_end = if_idx + 1, goto_end_idx
            else_start, else_end = idx_else + 1, lend


            then_is_break = loop_end_label and self._range_is_only_goto_to(then_start, goto_end_idx + 1, loop_end_label)
            then_will_emit = (then_is_break or self._range_will_emit(then_start, then_end, loop_start_label, loop_end_label))
            else_will_emit = self._range_will_emit(else_start, else_end, loop_start_label, loop_end_label)


            if not then_will_emit and else_will_emit:
                inv = f"(not {cond})"
                E(f"if {inv}:", base)
                self._emit_range(else_start, else_end, expr, E, indent=base + 1,
                                 loop_start_label=loop_start_label, loop_end_label=loop_end_label)
                return lend + 1

            # si ninguna rama emite, no generamos nada
            if not then_will_emit and not else_will_emit:
                return lend + 1

            # emitimos THEN
            E(f"if {cond}:", base)
            if then_is_break:
                E("break", base + 1)
            else:
                self._emit_range(then_start, then_end, expr, E, indent=base + 1,
                                 loop_start_label=loop_start_label, loop_end_label=loop_end_label)

            # ELSE sólo si va a emitir algo
            if else_will_emit:
                E("else:", base)
                self._emit_range(else_start, else_end, expr, E, indent=base + 1,
                                 loop_start_label=loop_start_label, loop_end_label=loop_end_label)

            return lend + 1

    def _emit_while_block(self, i, expr, E, base):
        start, cond_if_idx, goto_back_idx, lend = self.while_regions[i]
        cond = self._render_expr(self.tac[cond_if_idx]['arg1'], expr)
        body_start = cond_if_idx + 1
        body_end = goto_back_idx
        E(f"while {cond}:", base)

        loop_start_label = None
        if isinstance(self.tac[start].get('op'), str) and self.tac[start]['op'].endswith(':'):
            loop_start_label = self.tac[start]['op'][:-1]

        loop_end_label = None
        if isinstance(self.tac[lend].get('op'), str) and self.tac[lend]['op'].endswith(':'):
            loop_end_label = self.tac[lend]['op'][:-1]

        self._emit_range(body_start, body_end, expr, E, indent=base + 1,
                         loop_start_label=loop_start_label, loop_end_label=loop_end_label)
        return lend + 1

    def _emit_range(self, start, end, expr, E, indent, loop_start_label, loop_end_label):
        i = start
        while i < end:
            if i in self.func_regions:
                i = self._emit_function(i, expr, E); continue
            if i in self.if_regions:
                i = self._emit_if_block(i, expr, E, indent, loop_start_label, loop_end_label); continue
            if i in self.while_regions:
                i = self._emit_while_block(i, expr, E, indent); continue

            inst = self.tac[i]; op = inst.get('op')
            if isinstance(op, str) and op.endswith(':'):
                i += 1; continue

            if op == 'goto':
                tgt = inst.get('result')
                if loop_end_label and tgt == loop_end_label:
                    E("break", indent)
                elif loop_start_label and tgt == loop_start_label:
                    E("continue", indent)
                # otros goto no se traducen
            elif op == 'PARAM':
                self.call_args_buffer.append(self._render_expr(inst['arg1'], expr))
            elif op == 'CALL':
                fn = inst['arg1']; args = ", ".join(self.call_args_buffer); self.call_args_buffer.clear()
                if inst.get('result'): E(f"{inst['result']} = {fn}({args})", indent)
                else:                   E(f"{fn}({args})", indent)
            elif op == 'RETURN':
                if inst.get('arg1') is None: E("return", indent)
                else:                        E(f"return {self._render_expr(inst['arg1'], expr)}", indent)
            elif op == 'PRINT':
                E(f"print({self._render_expr(inst['arg1'], expr)})", indent)
            elif op == '=' and self._is_user(inst['result']):
                E(f"{inst['result']} = {self._render_expr(inst['arg1'], expr)}", indent)
            i += 1
        return i

    
    def _build_expr_map(self):
        expr = {}
        def set_expr(dst, e): expr[dst] = e
        for inst in self.tac:
            op = inst.get('op')
            if isinstance(op, str) and op.endswith(':'):
                continue
            if op == '=':
                set_expr(inst['result'], self._as_node(inst['arg1']))
            elif op == 'NOT':
                set_expr(inst['result'], ('not', self._as_node(inst['arg1'])))
            elif op in ('AND','OR','XOR','NEQ'):
                a = self._as_node(inst['arg1']); b = self._as_node(inst['arg2'])
                opm = {'AND':'and','OR':'or','XOR':'xor','NEQ':'xor'}[op]
                set_expr(inst['result'], (opm, a, b))
            elif op in ('NAND','NOR','XNOR'):
                a = self._as_node(inst['arg1']); b = self._as_node(inst['arg2'])
                set_expr(inst['result'], ('call', op.lower(), [a, b]))
            elif op == 'INPUT':
                set_expr(inst['result'], ('input',))
        return expr

    def _as_node(self, token):
        if token is None: return ('lit', False)
        s = str(token)
        if s == 'true': return ('lit', True)
        if s == 'false': return ('lit', False)
        return ('var', s)

    def _render_expr(self, token_or_temp, expr):
        node = self._resolve_node(self._as_node(token_or_temp), expr, seen=set())
        return self._render_node(node)

    def _resolve_node(self, node, expr, seen):
        k = node[0]
        if k == 'var':
            name = node[1]
            if name in expr and name not in seen and not self._is_user(name):
                seen.add(name)
                return self._resolve_node(expr[name], expr, seen)
            return node
        if k in ('lit', 'input'): return node
        if k == 'not': return ('not', self._resolve_node(node[1], expr, seen))
        if k in ('and', 'or', 'xor'):
            a = self._resolve_node(node[1], expr, seen)
            b = self._resolve_node(node[2], expr, seen)
            return (k, a, b)
        if k == 'call':
            fn = node[1]
            args = [self._resolve_node(x, expr, seen) for x in node[2]]
            return ('call', fn, args)
        return node

    def _render_node(self, node):
        k = node[0]
        if k == 'lit': return "True" if node[1] else "False"
        if k == 'var': return node[1]
        if k == 'input': return "input().strip().lower() in ('true','1','t','yes','y')"
        if k == 'not': return f"(not {self._render_node(node[1])})"
        if k in ('and', 'or'):
            a = self._render_node(node[1]); b = self._render_node(node[2])
            op = 'and' if k == 'and' else 'or'
            return f"({a} {op} {b})"
        if k == 'xor':
            a = self._render_node(node[1]); b = self._render_node(node[2])
            return f"({a} != {b})"
        if k == 'call':
            fn = node[1]
            args = ", ".join(self._render_node(x) for x in node[2])
            return f"{fn}({args})"
        return "False"


    def _range_is_only_goto_to(self, start, end_exclusive, target_label):
        if target_label is None: return False
        items = []
        for idx in range(start, end_exclusive):
            op = self.tac[idx].get('op')
            if isinstance(op, str) and op.endswith(':'): continue
            items.append(self.tac[idx])
        if len(items) != 1: return False
        inst = items[0]
        return inst.get('op') == 'goto' and inst.get('result') == target_label

    def _preinit_needed_for_range(self, expr, start, end, only_module):
        used_before_assign = set()
        assigned = set()
        for idx in range(start, end):
            inst = self.tac[idx]
            op = inst.get('op')
            if isinstance(op, str) and (op.endswith(':') or op.startswith('FUNCTION ') or op.startswith('END FUNCTION')):
                continue
            for a in (inst.get('arg1'), inst.get('arg2')):
                if isinstance(a, str) and self._is_user(a) and a not in assigned:
                    used_before_assign.add(a)
            if inst.get('op') == '=' and self._is_user(inst.get('result')):
                assigned.add(inst['result'])

        if only_module and self.func_regions:
            func_spans = list(self.func_regions.values())
            def inside_any_func(idx):
                for _, s, e in func_spans:
                    if s <= idx <= e: return True
                return False
            module_used = set()
            for idx in range(start, end):
                if inside_any_func(idx): continue
                inst = self.tac[idx]
                for a in (inst.get('arg1'), inst.get('arg2'), inst.get('result')):
                    if isinstance(a, str) and self._is_user(a):
                        module_used.add(a)
            used_before_assign = {v for v in used_before_assign if v in module_used}

        return sorted(used_before_assign)

    def _is_user(self, name):
        if not (isinstance(name, str) and name.isidentifier()): return False
        if name.startswith('t') or name.startswith('L'): return False
        reserved = {
            'true','false','and','or','not','nand','nor','xor','xnor',
            'if','else','while','bool','void','input','print','return'
        }
        if name in reserved: return False
        if name in self.func_names: return False
        return True

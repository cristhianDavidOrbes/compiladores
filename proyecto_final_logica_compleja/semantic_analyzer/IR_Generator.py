class IR_Generator:
    def __init__(self):
        self.instructions = []
        self.tcount = 0
        self.lcount = 0

    def new_temp(self):
        t = f"t{self.tcount}"
        self.tcount += 1
        return t

    def new_label(self):
        l = f"L{self.lcount}"
        self.lcount += 1
        return l

    def add(self, op, arg1=None, arg2=None, result=None):
        self.instructions.append({'op': op, 'arg1': arg1, 'arg2': arg2, 'result': result})

    def __str__(self):
        out = ["## TAC"]
        for inst in self.instructions:
            op = inst['op']
            a = inst['arg1']
            b = inst['arg2']
            r = inst['result']
            if op in ('=', 'NOT', 'AND', 'NAND', 'OR', 'NOR', 'XOR', 'XNOR', 'NEQ'):
                if op == '=':
                    out.append(f"  {r} = {a}")
                elif op == 'NOT':
                    out.append(f"  {r} = NOT {a}")
                else:
                    out.append(f"  {r} = {a} {op} {b}")
            elif op == 'INPUT':
                out.append(f"  {r} = INPUT()")
            elif op == 'PRINT':
                out.append(f"  PRINT {a}")
            elif op == 'if_false_goto':
                out.append(f"  if_false {a} goto {r}")
            elif op == 'goto':
                out.append(f"  goto {r}")
            elif op.endswith(':'):
                out.append(f"{op}")
            elif op == 'PARAM':
                out.append(f"  PARAM {a}")
            elif op == 'CALL':
                if r:
                    out.append(f"  {r} = CALL {a} {b}")
                else:
                    out.append(f"  CALL {a} {b}")
            elif op == 'RETURN':
                if a is None:
                    out.append("  RETURN")
                else:
                    out.append(f"  RETURN {a}")
            elif op.startswith('END FUNCTION'):
                out.append(op)
        return "\n".join(out)

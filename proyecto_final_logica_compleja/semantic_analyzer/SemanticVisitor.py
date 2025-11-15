from generated.logicaVisitor import logicaVisitor
from generated.logicaParser import logicaParser
from .SymbolTable import SymbolTable, Symbol
from .IR_Generator import IR_Generator

BOOL_T = 'bool'
VOID_T = 'void'


class SemanticVisitor(logicaVisitor):
    def __init__(self):
        super().__init__()
        self.table = SymbolTable()
        self.ir = IR_Generator()
        self.current_function = None
        self.loop_end_stack = []  # para break;

    # ---------- util de tipos ----------
    def expect_bool(self, type_, ctx_desc="expresión"):
        if type_ != BOOL_T:
            print(f"Error Semántico: Se esperaba booleano en {ctx_desc}, se obtuvo '{type_}'.")
            return False
        return True

    # ---------- programa / bloques ----------
    # program: (functionDecl | declaration | statement)+ EOF
    def visitProgram(self, ctx: logicaParser.ProgramContext):
        for child in ctx.children[:-1]:
            self.visit(child)
        return None

    # block: '{' (declaration | statement)* '}'
    def visitBlock(self, ctx: logicaParser.BlockContext):
        self.table.enter("block")
        for ch in ctx.children[1:-1]:
            self.visit(ch)
        self.table.exit()
        return None

    # ---------- declaraciones y asignaciones ----------
    # declaration: 'bool' ID ('=' boolExpr)? ';'
    def visitDeclaration(self, ctx: logicaParser.DeclarationContext):
        name = ctx.ID().getText()
        self.table.define_var(name, BOOL_T)
        if ctx.boolExpr():
            typ, addr = self.visit(ctx.boolExpr())
            if self.expect_bool(typ, "inicialización"):
                self.ir.add('=', arg1=addr, result=name)
        return None

    # assignment: ID '=' boolExpr ';'
    def visitAssignment(self, ctx: logicaParser.AssignmentContext):
        name = ctx.ID().getText()
        sym = self.table.resolve(name)
        if sym is None:
            print(f"Error Semántico: La variable '{name}' no está declarada.")
            return None
        if sym.category != 'variable' or sym.type != BOOL_T:
            print(f"Error Semántico: Asignación inválida sobre '{name}'.")
            return None
        typ, addr = self.visit(ctx.boolExpr())
        if self.expect_bool(typ, "asignación"):
            self.ir.add('=', arg1=addr, result=name)
        return None

    # inputStmt: ID '=' 'input' '(' ')' ';'
    def visitInputStmt(self, ctx: logicaParser.InputStmtContext):
        name = ctx.ID().getText()
        sym = self.table.resolve(name)
        if sym is None:
            print(f"Error Semántico: La variable '{name}' no está declarada.")
            return None
        if sym.type != BOOL_T:
            print(f"Error Semántico: 'input()' solo asigna booleanos.")
            return None
        self.ir.add('INPUT', result=name)
        return None

    # printStmt: 'print' '(' boolExpr ')' ';'
    def visitPrintStmt(self, ctx: logicaParser.PrintStmtContext):
        typ, addr = self.visit(ctx.boolExpr())
        if self.expect_bool(typ, "print"):
            self.ir.add('PRINT', arg1=addr)
        return None

    # callStmt: functionCall ';'
    def visitCallStmt(self, ctx: logicaParser.CallStmtContext):
        self.visit(ctx.functionCall())
        return None

    # ---------- control de flujo ----------
    # ifStatement: 'if' '(' boolExpr ')' block ('else' block)?
    def visitIfStatement(self, ctx: logicaParser.IfStatementContext):
        typ, cond = self.visit(ctx.boolExpr())
        self.expect_bool(typ, "condición if")

        l_else = self.ir.new_label()
        l_end = self.ir.new_label()
        jump_target = l_else if ctx.ELSE() else l_end

        self.ir.add('if_false_goto', arg1=cond, result=jump_target)
        self.visit(ctx.block(0))
        if ctx.ELSE():
            self.ir.add('goto', result=l_end)
            self.ir.add(f"{l_else}:")
            self.visit(ctx.block(1))
        self.ir.add(f"{l_end}:")
        return None

    # whileStatement: 'while' '(' boolExpr ')' block
    def visitWhileStatement(self, ctx: logicaParser.WhileStatementContext):
        l_start = self.ir.new_label()
        l_end = self.ir.new_label()
        self.ir.add(f"{l_start}:")
        typ, cond = self.visit(ctx.boolExpr())
        self.expect_bool(typ, "condición while")
        self.ir.add('if_false_goto', arg1=cond, result=l_end)

        self.loop_end_stack.append(l_end)
        self.visit(ctx.block())
        self.loop_end_stack.pop()

        self.ir.add('goto', result=l_start)
        self.ir.add(f"{l_end}:")
        return None

    # Opcional — si tu gramática incluye: breakStmt: BREAK ';'
    def visitBreakStmt(self, ctx: logicaParser.BreakStmtContext):
        if not self.loop_end_stack:
            print("Error Semántico: 'break' fuera de un ciclo.")
            return None
        self.ir.add('goto', result=self.loop_end_stack[-1])
        return None

    # ---------- funciones ----------
    # functionDecl: (typeSpecifier | VOID) ID '(' paramList? ')' block
    def visitFunctionDecl(self, ctx: logicaParser.FunctionDeclContext):
        ret_type = VOID_T if ctx.VOID() else BOOL_T
        fname = ctx.ID().getText()

        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                pname = p.ID().getText()
                params.append(Symbol(name=pname, type_=BOOL_T, category='variable'))

        func_sym = self.table.define_func(fname, ret_type, params)

        self.ir.add(f"FUNCTION {fname}:")
        entry = self.ir.new_label()
        self.ir.add(f"{entry}:")

        self.current_function = func_sym
        self.table.enter(f"func_{fname}")

        for p in params:
            self.table.define_var(p.name, BOOL_T)
            self.ir.add('PARAM_RECEIVE', result=p.name)

        self.visit(ctx.block())

        # Solo insertar retorno por defecto si es función bool y no se garantizó return
        if func_sym.type == BOOL_T and not self._has_return(ctx.block()):
            self.ir.add('RETURN', arg1='false')

        self.table.exit()
        self.current_function = None
        self.ir.add(f"END FUNCTION {fname}")
        return None

    # functionCall: ID '(' argList? ')'
    def visitFunctionCall(self, ctx: logicaParser.FunctionCallContext):
        fname = ctx.ID().getText()
        sym = self.table.resolve(fname)
        if sym is None or sym.category != 'function':
            print(f"Error Semántico: Llamada a función no declarada '{fname}'.")
            return ('error', None)

        args = []
        if ctx.argList():
            for e in ctx.argList().boolExpr():
                t, a = self.visit(e)
                if not self.expect_bool(t, f"argumento de '{fname}'"):
                    return ('error', None)
                args.append(a)

        if len(args) != len(sym.params):
            print(f"Error Semántico: La función '{fname}' esperaba {len(sym.params)} argumentos y recibió {len(args)}.")
            return ('error', None)

        for a in args:
            self.ir.add('PARAM', arg1=a)

        if sym.type == VOID_T:
            self.ir.add('CALL', arg1=fname, arg2=str(len(args)))
            return (VOID_T, None)
        else:
            t = self.ir.new_temp()
            self.ir.add('CALL', arg1=fname, arg2=str(len(args)), result=t)
            return (BOOL_T, t)

    # returnStatement: 'return' boolExpr? ';'
    def visitReturnStatement(self, ctx: logicaParser.ReturnStatementContext):
        if self.current_function is None:
            print("Error Semántico: 'return' fuera de una función.")
            return None

        if ctx.boolExpr():
            t, a = self.visit(ctx.boolExpr())
            if self.current_function.type != BOOL_T:
                print("Error Semántico: 'return valor' en función void.")
            elif self.expect_bool(t, "return"):
                self.ir.add('RETURN', arg1=a)
        else:
            if self.current_function.type != VOID_T:
                print("Error Semántico: 'return;' en función no-void.")
            self.ir.add('RETURN')
        return None

    # ---------- expresiones ----------
    # boolExpr → orExpr
    def visitBoolExpr(self, ctx: logicaParser.BoolExprContext):
        return self.visit(ctx.orExpr())

    # orExpr: xorExpr ((OR | NOR | XNOR) xorExpr)*
    def visitOrExpr(self, ctx: logicaParser.OrExprContext):
        typ, addr = self.visit(ctx.xorExpr(0))
        self.expect_bool(typ, "expresión OR")
        ops = [c.getText() for c in ctx.children if hasattr(c, 'getText') and c.getText() in ('or', 'nor', 'xnor')]
        for i, op_txt in enumerate(ops, start=1):
            rt, ra = self.visit(ctx.xorExpr(i))
            self.expect_bool(rt, "operando OR")
            tmp = self.ir.new_temp()
            self.ir.add(op_txt.upper(), arg1=addr, arg2=ra, result=tmp)
            addr = tmp
        return (BOOL_T, addr)

    # xorExpr: andExpr ((XOR | NEQ | EQ) andExpr)*
    # (si no tienes EQ en la gramática, quita el caso '==')
    def visitXorExpr(self, ctx: logicaParser.XorExprContext):
        typ, addr = self.visit(ctx.andExpr(0))
        self.expect_bool(typ, "expresión XOR/!=/==")
        ops = [c.getText() for c in ctx.children if hasattr(c, 'getText') and c.getText() in ('xor', '!=', '==')]
        for i, op_txt in enumerate(ops, start=1):
            rt, ra = self.visit(ctx.andExpr(i))
            self.expect_bool(rt, "operando XOR/!=/==")
            tmp = self.ir.new_temp()
            if op_txt == 'xor' or op_txt == '!=':
                self.ir.add('XOR' if op_txt == 'xor' else 'NEQ', arg1=addr, arg2=ra, result=tmp)
            else:
                self.ir.add('XNOR', arg1=addr, arg2=ra, result=tmp)  # a == b ≡ xnor(a,b)
            addr = tmp
        return (BOOL_T, addr)

    # andExpr: unaryExpr ((AND | NAND) unaryExpr)*
    def visitAndExpr(self, ctx: logicaParser.AndExprContext):
        typ, addr = self.visit(ctx.unaryExpr(0))
        self.expect_bool(typ, "expresión AND/NAND")
        ops = [c.getText() for c in ctx.children if hasattr(c, 'getText') and c.getText() in ('and', 'nand')]
        for i, op_txt in enumerate(ops, start=1):
            rt, ra = self.visit(ctx.unaryExpr(i))
            self.expect_bool(rt, "operando AND/NAND")
            tmp = self.ir.new_temp()
            self.ir.add(op_txt.upper(), arg1=addr, arg2=ra, result=tmp)
            addr = tmp
        return (BOOL_T, addr)

    # unaryExpr: (NOT | BANG) unaryExpr | primary
    def visitUnaryExpr(self, ctx: logicaParser.UnaryExprContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        typ, addr = self.visit(ctx.unaryExpr())
        self.expect_bool(typ, "operador NOT")
        tmp = self.ir.new_temp()
        self.ir.add('NOT', arg1=addr, result=tmp)
        return (BOOL_T, tmp)

    # primary: builtinCall | functionCall | TRUE | FALSE | ID | '(' boolExpr ')'
    def visitPrimary(self, ctx: logicaParser.PrimaryContext):
        if ctx.builtinCall():
            return self.visit(ctx.builtinCall())
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        if ctx.TRUE():
            return (BOOL_T, 'true')
        if ctx.FALSE():
            return (BOOL_T, 'false')
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.table.resolve(name)
            if sym is None:
                print(f"Error Semántico: Identificador '{name}' no declarado.")
                return ('error', None)
            if sym.category != 'variable' or sym.type != BOOL_T:
                print(f"Error Semántico: '{name}' no es una variable booleana.")
                return ('error', None)
            return (BOOL_T, name)
        if ctx.boolExpr():
            return self.visit(ctx.boolExpr())
        return ('error', None)

    # builtinCall: (NAND | NOR | XNOR) '(' boolExpr ',' boolExpr ')'
    def visitBuiltinCall(self, ctx: logicaParser.BuiltinCallContext):
        fname = ctx.start.text  # 'nand' | 'nor' | 'xnor'
        # Con la gramática actual SIEMPRE hay DOS boolExpr posicionales
        t1, a1 = self.visit(ctx.boolExpr(0))
        t2, a2 = self.visit(ctx.boolExpr(1))
        if not self.expect_bool(t1, f"argumento 1 de '{fname}'"):
            return ('error', None)
        if not self.expect_bool(t2, f"argumento 2 de '{fname}'"):
            return ('error', None)
        t = self.ir.new_temp()
        self.ir.add(fname.upper(), arg1=a1, arg2=a2, result=t)
        return (BOOL_T, t)

    # ---------- análisis de retorno garantizado ----------
    def _has_return(self, block_ctx):
        """
        Devuelve True si el bloque contiene un 'return' directo
        o si TODAS las rutas de un 'if ... else ...' retornan.
        Nota: returns dentro de 'while' NO garantizan salida.
        """
        for stmt in block_ctx.statement():
            # return directo
            if stmt.returnStatement() is not None:
                return True

            # if con ambas ramas retornando
            if stmt.ifStatement() is not None:
                ifs = stmt.ifStatement()
                then_has = self._has_return(ifs.block(0))
                else_has = False
                if ifs.ELSE() is not None and ifs.block(1) is not None:
                    else_has = self._has_return(ifs.block(1))
                if then_has and else_has:
                    return True

            # while no cuenta para todas las rutas
        return False

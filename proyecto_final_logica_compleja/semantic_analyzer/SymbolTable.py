class Symbol:
    def __init__(self, name, type_, category, params=None):
        self.name = name
        self.type = type_
        self.category = category
        self.params = params if params is not None else []

    def __repr__(self):
        if self.category == 'function':
            ps = ", ".join([f"{p.type} {p.name}" for p in self.params])
            return f"<Func {self.type} {self.name}({ps})>"
        return f"<Var {self.type} {self.name}>"


class Scope:
    def __init__(self, name="scope", enclosing=None):
        self.name = name
        self.symbols = {}
        self.enclosing = enclosing

    def insert(self, sym: Symbol):
        if sym.name in self.symbols:
            return False
        self.symbols[sym.name] = sym
        return True

    def lookup_local(self, name):
        return self.symbols.get(name)

    def lookup(self, name):
        s = self.lookup_local(name)
        if s:
            return s
        if self.enclosing:
            return self.enclosing.lookup(name)
        return None


class SymbolTable:
    def __init__(self):
        self.current = Scope("global", None)

    def enter(self, name="block"):
        self.current = Scope(name, self.current)

    def exit(self):
        if self.current.enclosing:
            self.current = self.current.enclosing

    def define_var(self, name, type_):
        sym = Symbol(name=name, type_=type_, category='variable')
        ok = self.current.insert(sym)
        if not ok:
            print(f"Error Semántico: La variable '{name}' ya está definida en este ámbito.")
        return sym

    def define_func(self, name, ret_type, params):
        sym = Symbol(name=name, type_=ret_type, category='function', params=params)
        ok = self.current.insert(sym)
        if not ok:
            print(f"Error Semántico: La función '{name}' ya está definida en este ámbito.")
        return sym

    def resolve(self, name):
        return self.current.lookup(name)

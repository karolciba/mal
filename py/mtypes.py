import menv
from utils import debug

class MalType(object):
    def __init__(self):
        pass
    def __str__(self):
        return "[base]"

class FunctionType(MalType):
    def __init__(self, env, binds, exprs):
        self.binds = binds
        self.exprs = exprs
        self.env = env
    def __str__(self):
        return "#function"

class AtomType(MalType):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return "<AtomType: {}>".format(self.value)

class IntType(MalType):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return "<AtomType: {}>".format(self.value)

class ListType(MalType):
    def __init__(self, data = None):
        if not data:
            data = []
        self.data = data
        # TODO: remove after refactoring in eval
        self.value = None
    def append(self, typ):
        self.data.append(typ)
    def __str__(self):
        s = "("
        s += " ".join(str(x) for x in self.data)
        return s + ")"
    def __repr__(self):
        s = "<ListType({}): ".format(len(self.data))
        s += " ".join(repr(x) for x in self.data)
        s += ">"
        return s
    def car(self):
        return self.data[0]
    def cdr(self):
        # debug("ListType#cdr {}".format(repr(self.data)))
        return ListType(self.data[1:])

class NilType(ListType):
    def __str__(self):
        return "nil"
    def __repr__(self):
        return "<NilType>"

nil_atom = NilType()
true_atom = AtomType('t')
false_atom = ListType()
pls_atom = AtomType('+')
min_atom = AtomType('-')
mul_atom = AtomType('*')
div_atom = AtomType('/')


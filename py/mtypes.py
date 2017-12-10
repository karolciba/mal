from utils import debug

class MalType(object):
    def __init__(self):
        pass
    def __str__(self):
        return "[base]"

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

def NilType():
    return ListType()

pls_atom = AtomType('+')
min_atom = AtomType('-')
mul_atom = AtomType('*')
div_atom = AtomType('/')


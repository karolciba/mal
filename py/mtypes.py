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
    def __init__(self):
        self._data = []
        pass
    def append(self, typ):
        self._data.append(typ)
    def __str__(self):
        s = "("
        s += " ".join(str(x) for x in self._data)
        return s + ")"
    def __repr__(self):
        s = "<ListType({}): ".format(len(self._data))
        s += " ".join(repr(x) for x in self._data)
        s += ">"
        return s

def NilType():
    return ListType()

pls_atom = AtomType('+')
min_atom = AtomType('-')
mul_atom = AtomType('*')
div_atom = AtomType('/')


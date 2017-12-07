class MalType(object):
    def __init__(self):
        pass
    def __str__(self):
        return "[base]"

class NilType(MalType):
    def __str__(self):
        return ""

class AtomType(MalType):
    def __init__(self, value):
        self._value = value
    def __str__(self):
        return str(self._value)

class IntType(MalType):
    def __init__(self, value):
        self._value = int(value)
    def __str__(self):
        return str(self._value)

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

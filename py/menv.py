import mtypes
from utils import debug

class Env(object):
    def __init__(self, outer = None, binds = None, exprs = None):
        debug("Env#__init__({}, binds={}, exprs={})".format(repr(outer), repr(binds), repr(exprs)))
        self.data = {}
        self.outer = outer
        if not binds:
            binds = mtypes.ListType()
        if not exprs:
            exprs = mtypes.ListType()

        pairs = zip(binds.data, exprs.data)
        for p in pairs:
            self.set(p[0],p[1])

    def set(self, key, value):
        debug("Env#set({},{})".format(repr(key),repr(value)))
        self.data[key.value] = value

    def find(self, key):
        if key.value in self.data:
            return self
        if self.outer:
            return self.outer.find(key)
        return mtypes.NilType()

    def get(self, key):
        debug("Env#get({})".format(repr(key)))
        v = self.data.get(key.value)
        if not v and self.outer:
            return self.outer.get(key)
        if v:
            return v
        raise Exception("'{}' not found".format(repr(key.value)))

    def __repr__(self):
        s = "<Env (): ({})>".format(repr(self.data))
        return s

import operator

def get_base_env():
    env = Env()
    appl = lambda op: lambda a,b: mtypes.AtomType(op(int(a.value),int(b.value)))
    env.set(mtypes.pls_atom, appl(operator.add))
    env.set(mtypes.min_atom, appl(operator.sub))
    env.set(mtypes.mul_atom, appl(operator.mul))
    env.set(mtypes.div_atom, appl(operator.floordiv))
    env.set(mtypes.true_atom, mtypes.true_atom)
    return env

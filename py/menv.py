import mtypes

class Env(object):
    def __init__(self, outer = None):
        self.data = {}
        self.outer = outer

    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        if self.outer:
            return self.outer.find(key)
        return mtypes.NilType()

    def get(self, key):
        v = self.data.get(key)
        if not v and self.outer:
            return self.outer.get(key)
        if v:
            return v
        raise Exception("'{}' not found".format(repr(key.value)))

import operator

def get_base_env():
    env = Env()
    appl = lambda op: lambda a,b: mtypes.AtomType(op(int(a.value),int(b.value)))
    env.set(mtypes.pls_atom, appl(operator.add))
    env.set(mtypes.min_atom, appl(operator.sub))
    env.set(mtypes.mul_atom, appl(operator.mul))
    env.set(mtypes.div_atom, appl(operator.floordiv))
    return env

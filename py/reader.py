from mtypes import *
from utils import debug

def read_str(data):
    debug("DEBUG data {}".format(data))
    tokens = tokenizer(data)
    debug("DEBUG tokens {}".format(tokens))
    reader = Reader(tokens)
    ast = reader.read_form()
    debug("DEBUG ast {}".format(ast))
    return ast

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

SYMBOLS = {}

EOL = chr(0x0)
DEBUG = not True

class Reader(object):
    def __init__(self, data):
        self._data = data if data else []
        self._data.append(EOL)
        self._i = 0
        pass

    def next(self):
        token = self._data[self._i]
        self._i += 1
        return token

    def peek(self):
        return self._data[self._i]

    def read_form(self):
        debug("DEBUG read_form peek {}".format(self.peek()))
        p = self.peek()
        if p == EOL:
            debug("returning EOL {}".format(p))
            return None
        elif p == '':
            debug("returning '' {}".format(p))
            return None
        elif p == '(':
            self.next()
            return self.read_list()
        else:
            return self.read_atom()

    def read_list(self):
        debug("DEBUG read_list peek {}".format(self.peek()))
        l = ListType()
        while True:
            p = self.peek()
            if self._i == len(self._data):
                return NilType()
            if p == EOL:
                return NilType()
            elif p == ')':
                self.next()
                debug("returning {}".format(l))
                return l
            else:
                debug("appending {}".format(l))
                v = self.read_form()
                if not v:
                    # raise "Exception"
                    return l
                else:
                    l.append(v)

    def read_atom(self):
        """MAL TYPES: -int-, -symbol-, keyword, vector, hash-map and atom"""
        debug("DEBUG read_atom peek {}".format(self.peek()))
        n = self.next()
        if check_int(n):
            debug("returning int {}".format(n))
            return IntType(int(n))
        elif n == '+':
            return pls_atom
        elif n == '-':
            return min_atom
        elif n == '*':
            return mul_atom
        elif n == '/':
            return div_atom
        elif n == 'true':
            return true_atom
        elif n == 'false':
            return false_atom
        elif n == 'nil':
            return nil_atom
        else:
            SYMBOLS[n] = True
            debug("returning atom {}".format(n))
            return AtomType(n)


import re

def tokenizer(data):
    regex = """[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)"""
    return re.findall(regex,data)

if __name__ == "__main__":
    from printer import *

    print(dg_str(read_str('(+ 1 2)')))
    print(dg_str(read_str('1')))
    print(dg_str(read_str("(1 2")))

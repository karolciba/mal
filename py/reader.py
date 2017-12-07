from mtypes import *

def read_str(data):
    DEBUG and print("DEBUG data {}".format(data))
    tokens = tokenizer(data)
    DEBUG and print("DEBUG tokens {}".format(tokens))
    reader = Reader(tokens)
    ast = reader.read_form()
    DEBUG and print("DEBUG ast {}".format(ast))
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
        DEBUG and print("DEBUG read_form peek {}".format(self.peek()))
        p = self.peek()
        if p == EOL:
            DEBUG and print("returning EOL {}".format(p))
            return None
        elif p == '':
            DEBUG and print("returning '' {}".format(p))
            return None
        elif p == '(':
            self.next()
            return self.read_list()
        else:
            return self.read_atom()

    def read_list(self):
        DEBUG and print("DEBUG read_list peek {}".format(self.peek()))
        l = ListType()
        while True:
            p = self.peek()
            if self._i == len(self._data):
                return NilType()
            if p == EOL:
                return NilType()
            elif p == ')':
                self.next()
                DEBUG and print("returning {}".format(l))
                return l
            else:
                DEBUG and print("appending {}".format(l))
                v = self.read_form()
                if not v:
                    # raise "Exception"
                    return l
                else:
                    l.append(v)

    def read_atom(self):
        """MAL TYPES: -int-, -symbol-, keyword, vector, hash-map and atom"""
        DEBUG and print("DEBUG read_atom peek {}".format(self.peek()))
        n = self.next()
        if check_int(n):
            DEBUG and print("returning int {}".format(n))
            return IntType(int(n))
        else:
            SYMBOLS[n] = True
            DEBUG and print("returning atom {}".format(n))
            return AtomType(n)


import re

def tokenizer(data):
    regex = """[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)"""
    return re.findall(regex,data)

if __name__ == "__main__":
    from printer import *

    print(pr_str(read_str('(+ 1 2)')))
    print(pr_str(read_str('1')))
    print(pr_str(read_str("(1 2")))

def f_read(str):
    return str

def f_eval(ast,env):
    return ast

def f_print(exp):
    return exp

def f_rep(str):
    return f_print(f_eval(f_read(str),""))

import sys


print("user> ", end='', flush=True)

for line in sys.stdin:
    print(f_rep(line), end='')
    print("user> ", end='', flush=True)


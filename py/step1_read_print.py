import reader
import printer

def f_read(data):
    return reader.read_str(data)

def f_eval(ast,env):
    return ast

def f_print(exp):
    return printer.pr_str(exp) + "\n"

def f_rep(str):
    return f_print(f_eval(f_read(str),repl_env))

import sys

repl_env = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a//b
        }


print("user> ", end='', flush=True)

for line in sys.stdin:
    print(f_rep(line), end='')
    print("user> ", end='', flush=True)


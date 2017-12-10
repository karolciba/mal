import reader
import printer
import mtypes
import menv

from utils import debug

repl_env = menv.get_base_env()

def f_read(data):
    return reader.read_str(data)

def f_eval(ast,env):
    debug("f_eval {}".format(repr(ast)))
    if type(ast) != mtypes.ListType:
        return f_eval_ast(ast, env)

    if len(ast.data) == 0:
        return ast

    ev_list = f_eval_ast(ast, env)
    op = ev_list.data[0]
    return op(*ev_list.data[1:])


def f_print(exp):
    return printer.pr_str(exp) + "\n"

def f_rep(str):
    return f_print(f_eval(f_read(str),repl_env))

def f_eval_ast(ast,env):
    debug("f_eval_ast {}".format(repr(ast)))
    if type(ast) == mtypes.AtomType:
        return env.get(ast)

    if type(ast) == mtypes.ListType:
        nlist = mtypes.ListType()
        for el in ast.data:
            nlist.append(f_eval(el,env))
        return nlist

    return ast

import sys


print("user> ", end='', flush=True)

for line in sys.stdin:
    try:
        print(f_rep(line), end='')
    except Exception as e:
        print(e)
    print("user> ", end='', flush=True)


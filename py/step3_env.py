import reader
import printer
import mtypes
import menv

from utils import debug

repl_env = menv.get_base_env()

def f_read(data):
    return reader.read_str(data)

def f_eval(ast,env):
    debug("f_eval {} with env {}".format(repr(ast), repr(env)))
    if type(ast) != mtypes.ListType:
        return f_eval_ast(ast, env)

    if len(ast.data) == 0:
        return ast

    arg = ast.car()

    if arg.value == "def!":
        debug("def! {}".format(repr(ast)))
        data = ast.cdr()
        key = data.car()
        value = f_eval_ast(data.cdr(), env)
        env.set(key,value.data[0])
        return value.data[0]
    elif arg.value == "let*":
        debug("let* {}".format(repr(ast)))
        data = ast.cdr()
        let_env = menv.Env(env)
        binds = data.car()
        params = data.cdr().data[0]
        for i in range(0, len(binds.data), 2):
            a = binds.data[i]
            b = binds.data[i+1]
            let_env.set(a, f_eval(b, let_env))
        debug("let_env {}".format(repr(let_env.data)))
        return f_eval(params, let_env)
    elif arg.value == "env":
        print("env: {}".format(env.data))
        return arg
    elif arg.value == 'pdb':
        import pdb; pdb.set_trace()
        return arg
    else:
        ev_list = f_eval_ast(ast, env)
        op = ev_list.car()
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


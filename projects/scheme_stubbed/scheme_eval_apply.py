import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    if self_evaluating(expr):
        return expr
    elif scheme_symbolp(expr):
        return env.lookup(expr)

    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    operator, operand = expr.first, expr.rest

    if scheme_symbolp(operator) and operator in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[operator](operand, env)
    else:
        # print('DEBUG:', expr)
        procedure = scheme_eval(operator, env)
        if isinstance(procedure, MacroProcedure):
            args = operand
            result = scheme_eval(complete_apply(procedure, args, env), env)
        else:
            args = operand.map(lambda x: scheme_eval(x, env))
            # print('DEBUG:', procedure)
            result = scheme_apply(procedure, args, env)
        return result
    # END Problem 1/2


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # BEGIN Problem 1/2
    "*** YOUR CODE HERE ***"
    validate_procedure(procedure)

    if isinstance(procedure, BuiltinProcedure):
        arg_list = []
        while args is not nil:
            arg_list.append(args.first)
            args = args.rest
        if procedure.need_env:
            arg_list.append(env)
        try:
            return procedure.py_func(*arg_list)
        except TypeError as err:
            raise SchemeError(f'incorrect number of arguments: {procedure}')
    elif isinstance(procedure, LambdaProcedure):
        child_frame = procedure.env.make_child_frame(procedure.formals, args)
        # print('DEBUG:', procedure.formals, args)
        # print('DEBUG:', procedure.body)
        return eval_all(procedure.body, child_frame)
    elif isinstance(procedure, MuProcedure):
        child_frame = env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child_frame)


def eval_all(expr, env):
    # print('DEBUG:', expr)
    if expr is nil:
        return None
    while expr.rest is not nil:
        # print('DEBUG:', expr.first)
        scheme_eval(expr.first, env)
        expr = expr.rest
    # print('DEBUG:', expr.first)
    return scheme_eval(expr.first, env, True)
    # END Problem 1/2


##################
# Tail Recursion #
##################

# Make classes/functions for creating tail recursive programs here!
# BEGIN Problem EC
"*** YOUR CODE HERE ***"
class Unevaluated:
    def __init__(self, expr, env):
        self.expr = expr
        self.env = env
# END Problem EC


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not Unevaluated.
    Right now it just calls scheme_apply, but you will need to change this
    if you attempt the extra credit."""
    validate_procedure(procedure)
    # BEGIN
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    return val
    # END


def optimized_tail_calls(unoptimized_scheme_eval):
    def optimized_eval(expr, env, tails=False):
        # if tails and not scheme_symbolp(expr) and not self_evaluating(expr):
        #     return Unevaluated(expr, env)
        if tails: 
            return Unevaluated(expr, env)
        result = unoptimized_scheme_eval(expr, env)
        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result
    return optimized_eval

scheme_eval = optimized_tail_calls(scheme_eval)

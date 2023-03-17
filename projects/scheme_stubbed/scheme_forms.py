from scheme_eval_apply import *
from scheme_utils import *
from scheme_classes import *
from scheme_builtins import *

#################
# Special Forms #
#################

"""
How you implement special forms is up to you. We recommend you encapsulate the
logic for each special form separately somehow, which you can do here.
"""

# BEGIN PROBLEM 1/2/3
"*** YOUR CODE HERE ***"
def do_define_form(expr, env):
    validate_form(expr, 2)
    signature = expr.first
    if scheme_symbolp(signature):
        validate_form(expr, 2, 2)
        env.define(signature, scheme_eval(expr.rest.first, env))
    elif scheme_listp(signature) and scheme_symbolp(signature.first):
        env.define(signature.first, do_lambda_form(Pair(signature.rest, expr.rest), env))
        return signature.first
    else:
        raise SchemeError
    return signature


def do_quote_form(expr, env):
    return expr.first


def do_begin_form(expr, env):
    validate_form(expr, 1)
    return eval_all(expr, env)


def do_lambda_form(expr, env):
    validate_form(expr, 2)
    return LambdaProcedure(expr.first, expr.rest, env)


def do_and_form(expr, env):
    if expr is nil:
        return True
    while expr.rest is not nil:
        result = scheme_eval(expr.first, env)
        if is_scheme_false(result):
            return result
        expr = expr.rest
    return scheme_eval(expr.first, env, True)


def do_or_form(expr, env):
    if expr is nil:
        return False
    while expr.rest is not nil:
        result = scheme_eval(expr.first, env)
        if is_scheme_true(result):
            return result
        expr = expr.rest
    return scheme_eval(expr.first, env, True)

def do_if_form(expr, env):
    validate_form(expr, 2)
    if is_scheme_true(scheme_eval(expr.first, env)):
        return scheme_eval(expr.rest.first, env, True)
    elif len(expr) == 3:
        return scheme_eval(expr.rest.rest.first, env, True)


def do_cond_form(expr, env):
    while expr is not nil:
        validate_form(expr.first, 1)
        predicate = True if expr.first.first == 'else' else scheme_eval(expr.first.first, env)
        if is_scheme_true(predicate):
            return predicate if expr.first.rest is nil else eval_all(expr.first.rest, env)
        expr = expr.rest


def do_let_form(expr, env):
    validate_form(expr, 1)
    formals, vals = nil, nil
    first, rest = expr.first, expr.rest
    while first is not nil:
        # print('DEBUG:', first)
        validate_form(first.first, 2, 2)
        if not scheme_symbolp(first.first.first):
            raise SchemeError
        formals = Pair(first.first.first, formals)
        vals = Pair(scheme_eval(first.first.rest.first, env), vals)
        first = first.rest

    child_frame = env.make_child_frame(formals, vals)
    return eval_all(rest, child_frame)


def do_mu_form(expr, env):
    validate_form(expr, 2)
    return MuProcedure(expr.first, expr.rest)


def do_define_macro(expr, env):
    validate_form(expr, 2)
    signature = expr.first
    if scheme_listp(signature) and scheme_symbolp(signature.first):
        env.define(signature.first, MacroProcedure(signature.rest, expr.rest, env))
        return signature.first
    else:
        raise SchemeError


SPECIAL_FORMS = {
        'define': do_define_form,
        'quote': do_quote_form,
        'begin': do_begin_form,
        'lambda': do_lambda_form,
        'and': do_and_form,
        'or': do_or_form,
        'if': do_if_form,
        'cond': do_cond_form,
        'let': do_let_form,
        'mu': do_mu_form,
        'define-macro': do_define_macro,
        }
# END PROBLEM 1/2/3

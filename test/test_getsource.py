import inspect, ast

def test():
    a = 10
    return a

a = ast.parse(inspect.getsource(test))
print(ast.dump(a))

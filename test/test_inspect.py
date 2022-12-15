import inspect

def test_inspect():
    a = 1
    print(inspect.stack()[2][0].f_locals)

def layer2():
    a = 1
    b = 2
    test_inspect()

layer2()

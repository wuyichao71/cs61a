import inspect

def test_inspect():
    a = 1
    # print(inspect.stack()[2][0].f_locals)
    print(inspect.stack())

def layer2():
    a = 1
    b = 2
    test_inspect()

def layer1():
    a = 1
    def layer2():
        p = inspect.stack()
        for i in range(len(p)):
            print(p[i][0].f_locals)
    return layer2

f = layer1()
f()

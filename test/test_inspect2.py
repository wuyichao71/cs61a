import inspect


n = 1

def f():
    a = 0
    def g():
        b = 1
        print(dir(inspect.currentframe().f_code))
        print(inspect.currentframe().f_locals)
        print(inspect.currentframe().f_globals)
        print(inspect.getframeinfo(inspect.currentframe()))
        return 0
    return g

k = f()
k()

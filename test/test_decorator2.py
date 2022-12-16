def f(n):
    def g(fn):
        def w(x):
            return fn(x) + n
        return w
    return g

@f(3)
def h(x):
    return x*x

print(h(4))

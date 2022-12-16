def main(fn):
    if __name__ == '__main__':
        fn()
    return fn

@main
def test(a):
    return None

print(test)

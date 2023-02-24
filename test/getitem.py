class A:
    def __init__(self):
        self.data = [1,2,3,4]

    def __getitem__(self, i):
        return self.data[i]

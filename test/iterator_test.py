class Countdown_iterator:
    def __init__(self, start):
        self.start = start
    def __next__(self):
        if self.start > 0:
            tmp = self.start
            self.start -= 1
            return tmp
        else:
            raise StopIteration

class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return Countdown_iterator(self.start)



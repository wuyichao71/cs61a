class Car:
    num_wheels = 4
    def __init__(self, color):
        self.num_wheels = 5
        print(self.num_wheels)
        print(Car.num_wheels)

a = Car('red')

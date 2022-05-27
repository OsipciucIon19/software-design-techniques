from abc import ABC, abstractmethod


class NoTurbo(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def accelerate(self): pass


class WithTurbo(NoTurbo):
    @abstractmethod
    def turbo_accelerate(self, _turbo):
        pass


class RegularCar(NoTurbo):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0

    def accelerate(self):
        self.speed += 1
        print("Car %s is accelerating" % self.name)


class SportsCar(WithTurbo):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0

    def accelerate(self):
        self.speed += 1
        print("Car %s is accelerating" % self.name)

    def turbo_accelerate(self, turbo):
        self.speed += turbo
        print("Car %s is accelerating with turbo %d" % (self.name, turbo))


if __name__ == '__main__':
    car = RegularCar('BMW')
    car.accelerate()

    autoCar = SportsCar('Audi')
    autoCar.turbo_accelerate(2)

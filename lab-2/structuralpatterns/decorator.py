from abc import ABCMeta


class AbstractCar(metaclass=ABCMeta):
    def get_cost(self) -> float: pass

    def get_parts(self): pass

    def get_tax(self):
        return 0.05 * self.get_cost()


class ConcreteCar(AbstractCar):
    def get_cost(self):
        return 10000

    def get_parts(self):
        return "initial car"


class AbstractCarDecorator(AbstractCar):
    def __init__(self, decorated_car):
        self.decorated_car = decorated_car

    def get_cost(self):
        return self.decorated_car.get_cost()

    def get_parts(self):
        return self.decorated_car.get_parts()


class Engine(AbstractCarDecorator):
    def __init__(self, decorated_car):
        AbstractCarDecorator.__init__(self, decorated_car)

    def get_cost(self):
        return self.decorated_car.get_cost() + 5000

    def get_parts(self):
        return self.decorated_car.get_parts() + " + engine"


class Turbocharger(AbstractCarDecorator):
    def __init__(self, decorated_car):
        AbstractCarDecorator.__init__(self, decorated_car)

    def get_cost(self):
        return self.decorated_car.get_cost() + 900

    def get_parts(self):
        return self.decorated_car.get_parts() + " + turbocharger"


class Exhaust(AbstractCarDecorator):
    def __init__(self, decorated_car):
        AbstractCarDecorator.__init__(self, decorated_car)

    def get_cost(self):
        return self.decorated_car.get_cost() + 500

    def get_parts(self):
        return self.decorated_car.get_parts() + " + exhaust"


if __name__ == "__main__":
    car = ConcreteCar()
    print(f"Parts ({car.get_parts()}):\n\t"
          f"Cost: ${car.get_cost()} | Sales tax: ${car.get_tax()}")

    car = Turbocharger(car)
    print(f"Parts ({car.get_parts()}):\n\t"
          f"Cost: ${car.get_cost()} | Sales tax: ${car.get_tax()}")

    car = Exhaust(car)
    print(f"Parts ({car.get_parts()}):\n\t"
          f"Cost: ${car.get_cost()} | Sales tax: ${car.get_tax()}")

    car = Engine(car)
    print(f"Parts ({car.get_parts()}):\n\t"
          f"Cost: ${car.get_cost()} | Sales tax: ${car.get_tax()}")

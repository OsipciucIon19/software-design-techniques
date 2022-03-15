class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1

        return car


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f'body: {self.__body.shape}')
        print(f'engine horsepower: {self.__engine.horsepower}')
        print(f'tire size: {self.__wheels[0].size}')


class Builder:
    def get_wheel(self): pass

    def get_engine(self): pass

    def get_body(self): pass


class JeepBuilder(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 85
        return engine

    def get_body(self):
        body = Body()
        body.shape = "hatchback"
        return body


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


if __name__ == "__main__":
    jeep_builder = JeepBuilder()
    nissan_builder = NissanBuilder()

    director = Director()

    print('Jeep')
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()

    print('Nissan')
    director.set_builder(nissan_builder)
    nissan = director.get_car()
    nissan.specification()

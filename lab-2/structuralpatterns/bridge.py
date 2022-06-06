from abc import ABCMeta


class Carrier(metaclass=ABCMeta):
    def carry_military(self, items):
        pass

    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print(f"The plane carries {items} military cargo goods")

    def carry_commercial(self, items):
        print(f"The plane carries {items} commercial cargo goods")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print(f"The plane carries {passengers} military passengers")

    def carry_commercial(self, passengers):
        print(f"The plane carries {passengers} commercial passengers")


class Plane:
    def __init__(self, carrier):
        self.carrier = carrier

    def display_description(self):
        pass

    def add_objects(self, new_objects):
        pass


class Commercial(Plane):
    def __init__(self, carrier, objects):
        super().__init__(carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Military(Plane):
    def __init__(self, carrier, objects):
        super().__init__(carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


if __name__ == "__main__":
    cargo = Cargo()
    passenger = Passenger()

    military_plane = Military(passenger, 100)
    military_plane.display_description()
    military_plane.add_objects(25)
    military_plane.display_description()

    commercialPlane = Commercial(cargo, 200)
    commercialPlane.display_description()

import math


class RoundHole:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius


class SquarePeg:
    def __init__(self, width):
        self.__width = width

    def get_width(self) -> float:
        return self.__width


class SquarePegAdapter:
    peg: SquarePeg

    def __init__(self, peg: SquarePeg):
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(5)
    round_peg = RoundPeg(5)

    print(f"Hole radius: {hole.get_radius()}\n")
    print(f"Round Peg radius: {round_peg.get_radius()}")
    print(f"The round peg fits the hole? {hole.fits(round_peg)}\n")

    sm_square_peg = SquarePeg(7)
    lg_square_peg = SquarePeg(10)

    sm_square_peg_adapter = SquarePegAdapter(sm_square_peg)
    lg_square_peg_adapter = SquarePegAdapter(lg_square_peg)
    print(f"Small peg radius: {sm_square_peg_adapter.get_radius()}")
    print(f"The small square peg fits the hole? {hole.fits(sm_square_peg_adapter)}")
    print(f"Large peg radius: {lg_square_peg_adapter.get_radius()}")
    print(f"The large square peg fits the hole? {hole.fits(lg_square_peg_adapter)}")

from Coords import Coords
from Energy import Energy


class Spring(Energy):

    def __init__(self, atom_no_1: int, atom_no_2: int, coords: Coords, d0: float, k: float):
        super().__init__(coords)
        self.__n1 = int(atom_no_1)
        self.__n2 = int(atom_no_2)
        self.__d0 = float(d0)
        self.__k = float(k)

    def __call__(self):
        d = (self._coords[self.__n1].dist(self._coords[self.__n2]) - self.__d0)
        return self.__k * d * d / 2

    @property
    def d0(self):
        return self.__d0

    @property
    def k(self):
        return self.__k

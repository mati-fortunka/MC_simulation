import math as m
from Coords import Coords
from Energy import Energy


class LennardJones(Energy):

    def __init__(self, atom_no_1: int, atom_no_2: int, coords: Coords, d0: float, disp_en: float):
        super().__init__(coords)
        self.__n1 = int(atom_no_1)
        self.__n2 = int(atom_no_2)
        self.__sigma = float(d0)
        self.__disp_en = -1 * float(disp_en)

    def __call__(self):
        d = self._coords[self.__n1].dist(self._coords[self.__n2])
        return 4 * self.__disp_en * (self.__sigma / m.pow(d, 6)) * (self.__sigma / m.pow(d, 6) - 1)

    @property
    def sigma(self):
        return self.__sigma

    @property
    def disp_en(self):
        return self.__disp_en

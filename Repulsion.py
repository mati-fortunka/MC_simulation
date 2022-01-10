import math as m
from Atom import Atom
from Coords import Coords
from Energy import Energy


class Repulsion(Energy):

    def __init__(self, coords: Coords, k: float):
        super().__init__(coords)
        self.__k = float(k)

    @property
    def k(self):
        return self.__k

    def __count(self, a1: Atom, a2: Atom):
        d = a1.dist(a2) / (a1.r + a2.r)
        if d < 1:
            return self.__k / m.pow(d, 12)
        else:
            return 0

    def __call__(self):
        energy = 0
        for idx, v in enumerate(self._coords):
            for j in range(idx + 1, self._coords.n_atoms):
                energy += self.__count(v, self._coords[j])
        return energy

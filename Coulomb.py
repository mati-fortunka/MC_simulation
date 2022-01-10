from Coords import Coords
from Energy import Energy


class Coulomb(Energy):

    def __init__(self, coords: Coords, k_c):
        super().__init__(coords)
        self.__k_c = float(k_c)

    @property
    def k_c(self):
        return self.__k_c

    def __count(self, a1, a2):
        return self.__k_c * a1.q * a2.q / a1.dist(a2)

    def __call__(self):
        energy = 0
        for i, v in enumerate(self._coords):
            if v.q != 0:
                for j in range(i + 1, self._coords.n_atoms):
                    if self._coords[j].q != 0:
                        energy += self.__count(v, self._coords[j])
        return energy

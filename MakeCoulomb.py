from Coords import Coords
from Coulomb import Coulomb
from Maker import Maker


class MakeCoulomb(Maker):

    def make(self, args, coords: Coords):
        return Coulomb(coords, args[1])

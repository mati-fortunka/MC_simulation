from Coords import Coords
from Maker import Maker
from Repulsion import Repulsion


class MakeRepulsion(Maker):

    def make(self, args, coords: Coords):
        return Repulsion(coords, args[1])

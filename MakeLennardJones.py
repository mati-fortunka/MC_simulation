from Coords import Coords
from LennardJones import LennardJones
from Maker import Maker


class MakeLennardJones(Maker):

    def make(self, args, coords: Coords):
        return LennardJones(args[1], args[2], coords, args[3], args[4])

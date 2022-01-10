from Coords import Coords
from Maker import Maker
from Spring import Spring


class MakeSpring(Maker):

    def make(self, args, coords: Coords):
        return Spring(args[1], args[2], coords, args[3], args[4])

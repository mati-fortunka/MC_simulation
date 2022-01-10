from Coords import Coords
from abc import ABC, abstractmethod


class Maker(ABC):

    @abstractmethod
    def make(self, args, coords: Coords):
        pass

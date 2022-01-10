from Coords import Coords
from abc import ABC, abstractmethod


class Energy(ABC):
    def __init__(self, coords: Coords):
        self._coords = coords

    @abstractmethod
    def __call__(self):
        pass

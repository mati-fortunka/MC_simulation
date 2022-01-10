from abc import ABC, abstractmethod

class Sink(ABC):

    def __init__(self, *args):
        pass

    @abstractmethod
    def __call__(self, *args):
        pass

from abc import ABC, abstractmethod
from Sink import Sink
from copy import deepcopy


class Observer(ABC):
    def __init__(self, *args):
        self._sink_list = []
        self._frequency = 1
        if len(args) != 0:
            for arg in args:
                if isinstance(arg, Sink):
                    self._sink_list.append(arg)
                else:
                    print(f"{arg} is not a Sink type")

    def add_sink(self, sink: Sink, *args):
        if isinstance(sink, Sink):
            self._sink_list.append(sink)
        else:
            print(f"{sink} is not a Sink type")
        if len(args) != 0:
            for arg in args:
                if isinstance(arg, Sink):
                    self._sink_list.append(arg)
                else:
                    print(f"{arg} is not a Sink type")

    @abstractmethod
    def observe(self, step: int):
        pass

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, n: int):
        if isinstance(n, int):
            self._frequency = n
        else:
            print(f"{n} is not an integer")

    set_frequency = frequency

    @property
    def sink_list(self):
        return deepcopy(self._sink_list)

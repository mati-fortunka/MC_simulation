import random
import math as m
from Coords import Coords
from TotalEnergy import TotalEnergy
from Observer import Observer


class MonteCarlo:
    def __init__(self, coords: Coords, total_en: TotalEnergy, T: float, observers: list = []):
        self.__T = T
        self.__coords = coords
        self.__max_step = 0.01
        self.__en = total_en
        self.__observer_list = observers
        self.__step = 0

    def make_observation(self):
        for oi in self.__observer_list:
            if self.__step % oi._frequency == 0:
                oi.observe(self.__step)

    def sample(self, n_steps):
        self.make_observation()
        for self.__step in range(1, n_steps+1):
            for j in range(self.__coords.n_atoms):
                dx = random.uniform(-self.__max_step, self.__max_step)
                dy = random.uniform(-self.__max_step, self.__max_step)
                old_x, old_y = self.__coords[j].x, self.__coords[j].y
                old_en = self.__en.energy()
                self.__coords[j].x = self.__coords[j].x + dx
                self.__coords[j].y = self.__coords[j].y + dy
                new_en = self.__en.energy()
                delta_e = new_en - old_en
                if delta_e > 0 and random.random() > m.exp(-delta_e / self.__T):
                    self.__coords[j].x = old_x
                    self.__coords[j].y = old_y
            self.make_observation()

    def add_observer(self, observer: Observer, *args):
        if isinstance(observer, Observer):
            self.__observer_list.append(observer)
        else:
            print(f"{observer} is not an Observer type")
        if len(args) != 0:
            for arg in args:
                if isinstance(arg, Observer):
                    self.__observer_list.append(arg)
                else:
                    print(f"{arg} is not an Observer type")

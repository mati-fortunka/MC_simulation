from Observer import Observer
from TotalEnergy import TotalEnergy


class EnergyObserver(Observer):

    def __init__(self, tot_en : TotalEnergy, *args):
        super().__init__(*args)
        self.__total_energy = tot_en

    def observe(self, step: int):
        output = f"{step}\t{self.__total_energy()}\n"
        for i in self._sink_list:
            i(output)

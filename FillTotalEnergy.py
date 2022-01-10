from Maker import Maker
from MakeCoulomb import MakeCoulomb
from MakeRepulsion import MakeRepulsion
from MakeSpring import MakeSpring
from TotalEnergy import TotalEnergy


class FillTotalEnergy(TotalEnergy):

    def __init__(self):
        # self.__dispatch = {"HARMONIC": MakeSpring(), "SPRING": MakeSpring(), "REPULSION": MakeRepulsion(),
        # "COULOMB": MakeCoulomb()}
        self.__dispatch = {"Spring": MakeSpring(), "Repulsion": MakeRepulsion(), "Coulomb": MakeCoulomb()}

    def fill(self, total_energy: TotalEnergy, filename: str):
        with open(filename) as f:
            lines = f.readlines()
        for i in lines:
            i = i.split()
            en = self.__dispatch[i[0]].make(i, total_energy._coords)
            total_energy.add_energy(en)

    def register_energy(self, energy_name: str, energy_maker: Maker):
        try:
            self.__dispatch[energy_name] = energy_maker
        except:
            print(f"{energy_maker} is not an Energy object maker or just does not work.")

from Energy import Energy


class TotalEnergy(Energy):

    def __init__(self, coords):
        super().__init__(coords)
        self.__Elist = []

    def add_energy(self, energy: Energy):
        if isinstance(energy, Energy):
            self.__Elist.append(energy)
        else:
            print(f"{energy} is not an Energy object")

    def remove_energy(self, energy: Energy):
        if isinstance(energy, Energy):
            self.__Elist.remove(energy)
        else:
            print(f"{energy} is not an Energy object")

    def __call__(self):
        self.__E = 0
        for i in self.__Elist:
            self.__E += i()
        return self.__E

    energy = __call__

from Atom import Atom


class Coords:

    def __init__(self, *atoms_list):
        self.__i = -1
        if len(atoms_list) == 0:
            self.__Alist = []
            print("No atom coordinates specified.")

        else:
            if isinstance(atoms_list[0], Atom):
                self.__Alist = [atoms_list[i] for i in range(len(atoms_list))]

            if isinstance(atoms_list[0], str):
                with open(atoms_list[0]) as f:
                    lines = f.readlines()
                self.__Alist = [lines[i].rstrip('\n').split() for i in range(len(lines))]
                self.__Alist = [[j for j in i] for i in self.__Alist]
                self.__Alist = [Atom(i) for i in self.__Alist]
        self.__n_atoms = len(self.__Alist)

    @property
    def n_atoms(self):
        return self.__n_atoms

    __len__ = n_atoms

    def __str__(self):
        template = "{0:5}{1:8}{2:8}{3:6}{4:5}{5:5}"
        output = template.format("no.", "X", "Y", "type", "R", "Q")
        output += "\n"

        for i, v in enumerate(self.__Alist):
            output += template.format(f"{i}", str(v.x), str(v.y), str(v.t), str(v.r), str(v.q))
            output += "\n"
        return output

    def __iter__(self):
        return self

    def __getitem__(self, i):
        return self.__Alist[i]

    def __next__(self):
        if self.__i + 1 < len(self.__Alist):
            self.__i += 1

            return self.__Alist[self.__i]
        else:
            self.__i = -1
            raise StopIteration()

    def add_atom(self, a: Atom):
        self.__Alist.append(a)

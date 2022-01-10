import math as m


class Atom:

    def __make_Atom(self, x, y, type="C", r=1, q=0):
        self.__x = float(x)
        self.__y = float(y)
        self.__t = str(type)
        self.__r = float(r)
        self.__q = float(q)

    def __init__(self, *args):
        if len(args) == 0:
            print("No values specified. Default values: x=0 y=0 type='C' r=1 q=0")
            self.__make_Atom(0, 0)

        else:
            if isinstance(args[0], list): args = args[0]
            if isinstance(args[0], int) or isinstance(args[0], float) or isinstance(args[0], str):
                if len(args) == 2:
                    self.__make_Atom(args[0], args[1])
                if len(args) == 3:
                    self.__make_Atom(args[0], args[1], args[2])
                if len(args) == 4:
                    self.__make_Atom(args[0], args[1], args[2], args[3])
                if len(args) == 5:
                    self.__make_Atom(args[0], args[1], args[2], args[3], args[4])

    def __str__(self):
        return f"{self.__x}\t{self.__y}\t{self.__t}\t{self.__r}\t{self.__q}"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, val):
        self.__x = val

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def t(self):
        return self.__t

    @property
    def r(self):
        return self.__r

    @property
    def q(self):
        return self.__q

    @property
    def q_signed_int(self):
        if self.__q > 0:
            sign = "+"
        elif self.__q == 0:
            return "  "
        else:
            sign = ""
        return sign + str(int(self.__q))

    def dist(self, a1):
        return m.sqrt((self.__x - a1.__x) * (self.__x - a1.__x) + (self.__y - a1.__y) * (self.__y - a1.__y))

    def new_position(self, x, y):
        self.__x = x
        self.__y = y

    def move_atom(self, a, b):
        self.__x += a
        self.__y += b

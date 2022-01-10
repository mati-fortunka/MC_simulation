from Coords import Coords
from Observer import Observer


class CoordsObserver(Observer):

    def __init__(self, coords: Coords, *args):
        super().__init__(*args)
        self._coords = coords

    def observe(self, step: int):
        coords_table = ""
        for j, a in enumerate(self._coords):
            line = f"{'ATOM':6s}{j+1:5d} {a.t:^4s}{'':1s}{'ARG':3s} {'A':1s}{1:4d}{'':1s}   {a.x:8.3f}{a.y:8.3f}{0:8.3f}{0.5:6.2f}{35.88:6.2f}          {a.t:>2s}{a.q_signed_int:2s}\n"
            #line = f"ATOM   {j+1:4d}  {a.t:4s} ARG A   1    {a.x:8.3f}{a.y:8.3f}{0:8.3f}  0.50 35.88           {a.t:1s}\n"
            coords_table += line
        output = f"MODEL    {step}\n{coords_table}ENDMDL\n"
        for i in self._sink_list:
            i(output)
from Coords import Coords
from CoordsObserver import CoordsObserver
from EnergyObserver import EnergyObserver
from FileSink import FileSink
from FillTotalEnergy import FillTotalEnergy
from MonteCarlo import MonteCarlo
from ScreenSink import ScreenSink
from TotalEnergy import TotalEnergy
from MakeLennardJones import MakeLennardJones

file_coord = "coords_and_output/benzene"
energy_file = "coords_and_output/benzene_en"
traj_file = "coords_and_output/trajectory_b.pdb"

coords = Coords(file_coord)
print(coords)

tot_energy = TotalEnergy(coords)
energy_fill = FillTotalEnergy()
energy_fill.register_energy("LennardJones", MakeLennardJones())
energy_fill.fill(tot_energy, energy_file)

screen_sink = ScreenSink()
file_sink_c = FileSink(traj_file)
en_obs_sc = EnergyObserver(tot_energy, screen_sink)
c_obs_f = CoordsObserver(coords, file_sink_c )

#en_file = "coords_and_output/en_out.dat"
#file_sink_en = FileSink(en_file)
#c_obs_sc = CoordsObserver(coords, screen_sink)
#en_obs_f = EnergyObserver(tot_energy, file_sink_en)
#mc = MonteCarlo(coords, tot_energy, 1, [en_obs_sc, c_obs_sc, en_obs_f, c_obs_f])

en_obs_sc.frequency = 10
mc = MonteCarlo(coords, tot_energy, 1, [en_obs_sc, c_obs_f])
mc.sample(1000)


file_coord = "coords_and_output/2_chains_coords"
energy_file = "coords_and_output/2_chains_en"
traj_file = "coords_and_output/trajectory.pdb"

coords = Coords(file_coord)
print(coords)

tot_energy = TotalEnergy(coords)
energy_fill = FillTotalEnergy()
energy_fill.fill(tot_energy, energy_file)

file_sink_c = FileSink(traj_file)
en_obs_sc = EnergyObserver(tot_energy, screen_sink)
c_obs_f = CoordsObserver(coords, file_sink_c)

en_obs_sc.frequency = 100
c_obs_f.frequency = 10
mc = MonteCarlo(coords, tot_energy, 0.1, [en_obs_sc, c_obs_f])
mc.sample(100000)


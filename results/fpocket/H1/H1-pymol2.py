import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/data/H1.pdb", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/results/fpocket/H1/pocket1_vert.pqr", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/results/fpocket/H1/pocket1_atm.pdb", quiet=False)

cmd.hide("sticks", "pocket1_vert")
cmd.show("surface", "pocket1_vert")
cmd.color("white", "pocket1_vert")
cmd.rebuild()

cmd.orient()

cmd.save("H1.pse")

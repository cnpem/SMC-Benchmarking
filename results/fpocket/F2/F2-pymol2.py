import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/data/F2.pdb", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/results/fpocket/F2/pocket37_vert.pqr", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/SMC-Benchmarking/results/fpocket/F2/pocket37_atm.pdb", quiet=False)

cmd.hide("sticks", "pocket37_vert")
cmd.show("surface", "pocket37_vert")
cmd.color("white", "pocket37_vert")
cmd.rebuild()

cmd.orient()

cmd.save("F2.pse")

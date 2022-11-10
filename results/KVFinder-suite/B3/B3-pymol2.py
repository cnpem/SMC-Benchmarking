import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("../../.././hosts/B3.pdb", quiet=False)
cmd.load("B3.KVFinder.output.pdb", quiet=False)
cmd.load("B3.surface.pdb", quiet=False)

cmd.hide("sticks", "B3.KVFinder.output")
cmd.show("spheres", "B3.KVFinder.output")
cmd.alter("obj B3.KVFinder.output", "vdw=0.125")
cmd.alter("obj B3.surface", "vdw=0.125")
cmd.rebuild()

stored.b = []
cmd.iterate("(obj B3.KVFinder.output)", "stored.b.append(b)")
cmd.spectrum("b", "blue_white_red", "B3.KVFinder.output", [min(stored.b), max(stored.b)])
cmd.ramp_new("Depth", "B3.KVFinder.output", [min(stored.b), max(stored.b)], ["blue", "white", "red"])

cmd.orient()

cmd.save("B3.pse")

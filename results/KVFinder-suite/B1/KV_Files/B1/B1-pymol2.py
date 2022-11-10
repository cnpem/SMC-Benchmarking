import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("../../../../.././hosts/B1.pdb", quiet=False)
cmd.load("B1.KVFinder.output.pdb", quiet=False)

cmd.hide("sticks", "B1.KVFinder.output")
cmd.show("spheres", "B1.KVFinder.output")
cmd.alter("obj B1.KVFinder.output", "vdw=0.125")
cmd.rebuild()

stored.b = []
cmd.iterate("(obj B1.KVFinder.output)", "stored.b.append(b)")
cmd.spectrum("b", "blue_white_red", "B1.KVFinder.output", [min(stored.b), max(stored.b)])
cmd.ramp_new("Depth", "B1.KVFinder.output", [min(stored.b), max(stored.b)], ["blue", "white", "red"])

cmd.orient()

cmd.save("B1.pse")

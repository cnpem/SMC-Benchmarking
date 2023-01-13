import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("../../../hosts/B10.pdb", quiet=False)
cmd.load("B10_surface-map_grid-0.6_rad1-1.4_rad2-8.0_full-structure.dx", quiet=False)

cmd.isomesh("cavities", "B10_surface-map_grid-0.6_rad1-1.4_rad2-8.0_full-structure", level=3.0) # Isolated cavitycmd.orient()

cmd.save("B10.pse")

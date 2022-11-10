import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("../../../hosts/O1.pdb", quiet=False)
cmd.load("O1_surface-map_grid-0.6_rad1-1.4_rad2-8.0_full-structure.dx", quiet=False)

cmd.isomesh("cavities", "O1_surface-map_grid-0.6_rad1-1.4_rad2-8.0_full-structure", level=1.5) # Molecular surfacecmd.orient()

cmd.save("O1.pse")

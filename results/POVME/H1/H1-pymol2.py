import pymol
from pymol import cmd, stored

pymol.finish_launching(["pymol", "-q"])

cmd.load("/home/jvsguerra/remote-repos/moc-benchmarking/data/H1.pdb", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/moc-benchmarking/results/POVME/H1/H1_frameInfo/H1_inclusion.pdb", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/moc-benchmarking/results/POVME/H1/H1_frameInfo/H1_volumetric_density.dx", quiet=False)
cmd.load("/home/jvsguerra/remote-repos/moc-benchmarking/results/POVME/H1/H1_frameInfo/H1_frame_1_surface.pdb", quiet=False)

cmd.show("dots", "H1_volumetric_density")

cmd.alter("obj H1_inclusion", "vdw=0.5")
cmd.alter("obj H1_frame_1_surface", "vdw=0.5")
cmd.rebuild()

cmd.orient()

# Fig. 3d of
# Victor Liu, Michelle Povinelli, and Shanhui Fan,
# "Resonance-enhanced optical forces between coupled photonic crystal slabs",
# Optics Express, Vol. 17, No. 24, 2009
# The frequency used in this file does not match exactly with the paper.

import numpy as np
import S4
import matplotlib.pyplot as plt

S = S4.New(Lattice=((1, 0),(0, 0)), NumBasis=27)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
S.SetMaterial(Name = 'Silicon', Epsilon = 12.0 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Vacuum')

S.SetRegionRectangle(
    Layer = 'Slab', 
    Material = 'Silicon', 
    Center = (0,0), 
    Angle = 0, 
    Halfwidths = (0.25,0.5))

S.AddLayerCopy(Name = 'Spacer', Thickness = 0.5, Layer = 'AirAbove')
S.AddLayerCopy(Name = 'Slab2', Thickness = 0.5, Layer = 'Slab')
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
                         Order = 0)

S.SetFrequency(0.63)

x_space = np.linspace(-0.5, 3.5, 200)
z_space = np.linspace(-1, 2.5, 175)

for x in x_space:
    for z in z_space:
        E, H = S.GetFields(x, 0, z)
        Ey = E[1]
        print(f'x: {x}  z: {z}  Ey: {Ey}')
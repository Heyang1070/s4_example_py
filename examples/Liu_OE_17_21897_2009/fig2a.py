# Fig. 2a of
# Victor Liu, Michelle Povinelli, and Shanhui Fan,
# "Resonance-enhanced optical forces between coupled photonic crystal slabs",
# Optics Express, Vol. 17, No. 24, 2009
# A factor of 0.5 due to time averaging is not taken into account here

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
S.AddLayer(Name = 'Slab2', Thickness = 0.5, Material = 'Vacuum')

S.SetRegionRectangle(
    Layer = 'Slab2', 
    Material = 'Silicon', 
    Center = (0.15,0), 
    Angle = 0, 
    Halfwidths = (0.25,0.5))

S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
                         Order = 0)

S.SetFrequency(0.57)

dx_space = np.linspace(-0.5, 0.5, 100)
for dx in dx_space:
    S.SetRegionRectangle(
    Layer = 'Slab2', 
    Material = 'Silicon', 
    Center = (dx,0), 
    Angle = 0, 
    Halfwidths = (0.25,0.5))

    T1x,T1y,T1z = S.GetStressTensorIntegral('Spacer', 0.5)
    T2x,T2y,T2z = S.GetStressTensorIntegral('AirBelow', 0)
    print(f'dx: {dx}  T2x-T1x: {T2x-T1x}  T2z-T1z: {T2z-T1z}')
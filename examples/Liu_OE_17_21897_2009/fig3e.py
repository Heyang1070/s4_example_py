# Fig. 3e of
# Victor Liu, Michelle Povinelli, and Shanhui Fan,
# "Resonance-enhanced optical forces between coupled photonic crystal slabs",
# Optics Express, Vol. 17, No. 24, 2009
# The extremely high Q resonance is not captured unless a very fine sampling is used.

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

S.AddLayerCopy(Name = 'Spacer', Thickness = 0.65, Layer = 'AirAbove')
S.AddLayerCopy(Name = 'Slab2', Thickness = 0.5, Layer = 'Slab')
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
                         Order = 0)

freq_space = np.linspace(0.25, 0.7, 450)
for freq in freq_space:
    S.SetFrequency(freq)

    forward, backward = S.GetPowerFlux(Layer = 'AirBelow', zOffset = 0)
    print(f'freq: {freq}  forward: {forward}')


# Bottom pane of Fig. 12 in
# Shanhui Fan and J. D. Joannopoulos,
# "Analysis of guided resonances in photonic crystal slabs",
# Phys. Rev. B, Vol. 65, 235112

import numpy as np
import S4
import matplotlib.pyplot as plt

S = S4.New(Lattice=((1, 0),(0, 1)), NumBasis=100)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
S.SetMaterial(Name = 'Silicon', Epsilon = 12.0 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Silicon')
S.SetRegionCircle(Layer = 'Slab', Material = 'Vacuum', 
                  Center = (0,0), Radius = 0.2)
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 1.0 + 0.0j, 
                         pAmplitude = 0 + 0j, 
                         Order = 0)

# UsePolarizationDecomposition
freq_space = np.linspace(0.25, 0.27, 10)

for freq in freq_space:
    S.SetFrequency(freq)

    # backward should be zero
    _, backward = S.GetPowerFlux(Layer = 'AirAbove', zOffset = 0)
    forward, _ = S.GetPowerFlux(Layer = 'AirBelow', zOffset = 0)
    print(f'freq : {freq}, forward : {forward},  backward : {backward}')

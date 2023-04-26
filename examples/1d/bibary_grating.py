# In a 1D pattern, the pattern should be specified only with rectangles.
# The y-dimension of the rectangles is ignored.

import numpy as np
import S4


S = S4.New(Lattice=((1, 0), (0, 0)), NumBasis=27)

# Material definition
S.SetMaterial(Name = 'Silicon', Epsilon = 12 + 0.0j)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Vacuum')
S.SetRegionRectangle(Layer = 'Slab', Material = 'Silicon', 
                     Center = (0,0), Angle = 0, 
                     Halfwidths = (0.25, 0))
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0.0 + 0.0j, 
                         pAmplitude = 1.0 + 0j, 
                         Order = 0)

# UsePolarizationDecomposition
freq_space = np.linspace(0.25, 0.7, 90)

for freq in freq_space:
    S.SetFrequency(freq)

    # backward should be zero
    forward, backward = S.GetPowerFlux(Layer = 'AirBelow', zOffset = 0)
    print(f'freq : {freq}, forward : {forward}')

import numpy as np
import S4

# In a 1D pattern, the pattern should be specified only with rectangles.
# The half-height of the rectangle should be 0.5/L where L is the lattice
# constant. (Assume a unit cell of unit area).

L = 1
S = S4.New(Lattice=((L, 0), (0, 0)), NumBasis=27)

# Material definition
S.SetMaterial(Name = 'Silicon', Epsilon = 12 + 0.0j)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Vacuum')
S.SetRegionRectangle(Layer = 'Slab', Material = 'Silicon', 
                     Center = (0,0), Angle = 0, 
                     Halfwidths = (0.25, 0.5/L))
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 1.0 + 0.0j, 
                         pAmplitude = 0.0 + 0j, 
                         Order = 0)

# Get reciprocal lattice coordinates of the Fourier series orders used
Glist = S.GetBasisSet()
print(Glist)

freq_space = np.linspace(0.25, 3.2, 590)

for freq in freq_space:
    S.SetFrequency(freq)

    # backward should be zero
    power = S.GetPowerFluxByOrder(Layer = 'AirBelow', zOffset = 0)
    print(f'{power}')
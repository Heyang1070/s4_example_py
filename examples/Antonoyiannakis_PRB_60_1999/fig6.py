# Reproduces one of the curves in Fig. 6 in
# M. I. Antonoyiannakis and J. B. Pendry,
# "Electromagnetic forces in photonic crystals",
# Phys. Rev. B, Vol. 60, No. 4, 1999.

import numpy as np
import S4


S = S4.New(Lattice=((1, 0), (0, 1)), NumBasis=1)

# Material definition
S.SetMaterial(Name = 'Eps1', Epsilon = 10 + 0j)
S.SetMaterial(Name = 'Eps2', Epsilon = 1 + 0j)
S.SetMaterial(Name = 'Eps3', Epsilon = 9 + 0j)

S.AddLayer(Name = 'Above', Thickness = 0, Material = 'Eps1')
S.AddLayer(Name = 'Slab', Thickness = 1, Material = 'Eps2')
S.AddLayer(Name = 'Below', Thickness = 0, Material = 'Eps3')

S.SetFrequency(0.01) # lambda/d = 100

phi_space = np.linspace(0, 89, 178)

for phi in phi_space:
    # E polarized along the grating periodicity direction
    S.SetExcitationPlanewave(IncidenceAngles=(phi, 0), 
                             sAmplitude = 1.0 + 0.0j, 
                             pAmplitude = 0.0 + 0j, 
                             Order = 0)
    
    T1x, T1y, T1z = S.GetStressTensorIntegral('Slab', 0.9)
    # We need to plot -T1z because the surface normal is in the 
    # -z direction.

    print(f'angle : {np.cos(np.pi*phi/180)}   T1z : {-T1z})')
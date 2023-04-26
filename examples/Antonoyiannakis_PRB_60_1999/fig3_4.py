# Reproduces Fig. 3 and 4 in
# M. I. Antonoyiannakis and J. B. Pendry,
# "Electromagnetic forces in photonic crystals",
# Phys. Rev. B, Vol. 60, No. 4, 1999.

import numpy as np
import S4


S = S4.New(Lattice=((1, 0), (0, 1)), NumBasis=1)

# Material definition
S.SetMaterial(Name = 'A1', Epsilon = 1 + 0j)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1 + 0j)

S.AddLayer(Name = 'Above', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Below', Thickness = 0, Material = 'A1')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 1.0 + 0.0j, 
                         pAmplitude = 0.0 + 0j, 
                         Order = 0)

f_p =15
gamma = 0.1
freq_space = np.linspace(1, 25, 120)

for freq in freq_space:
    S.SetFrequency(freq)

    epsr = 1 - f_p*f_p/(freq*freq + gamma*gamma)
    epsi = f_p*f_p/(freq*freq + gamma*gamma) * gamma/freq
    S.SetMaterial(Name = 'A1', Epsilon = epsr + epsi*1j)

    # Reflected power
    forward, reflected = S.GetPowerFlux(Layer = 'Above', zOffset = 0)
    reflected = -reflected/forward

    T1x, T1y, T1z = S.GetStressTensorIntegral('Above', 0)
    T2x, T2y, T2z = S.GetStressTensorIntegral('Below', 0)

    # We need to plot -T1z because the surface normal is in the 
    # -z direction.

    print(f'freq : {freq}  reflected : {reflected}  T1z : {-T1z}  T2z : {T2z}')
    

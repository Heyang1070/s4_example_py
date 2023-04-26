# nfinite halfspace of magneto-optic material.
# Assume the permittivity tensor in the receiving halfspace is
# [  e   ie' 0 ]
# [ -ie' e   0 ]
# [  0   0   e ]
# Then solving the wave equation gives two circular polarization modes:
# E = (1, i)/sqrt(2), km = omega sqrt(e-ie)
# E = (1,-i)/sqrt(2), kp = omega sqrt(e+ie)
# For normal incidence, we match boundary conditions:
# (E0+Erx, Ery) = a(1,i)/sqrt(2) + b(1,-i)/sqrt(2)
# k0(E0-Erx, -Ery) = a km(1,i)/sqrt(2) + b kp(1,-i)/sqrt(2)
# k0 = omega
# Solving these gives
# a = E0 k0/(k0+km)/sqrt(2), b = E0 k0/(k0+kp)/sqrt(2)
# Er = E0/((k0+km)(k0+kp))/sqrt(2) (k0 k0 - km kp, i k0(kp-km))/sqrt(2)
# The transmitted field is
# Etx = Re[   E0 k0/sqrt(2) (exp(i km z)/(k0+km) + exp(i kp z)/(k0+kp)) ]
# Ety = Re[ i E0 k0/sqrt(2) (exp(i km z)/(k0+km) - exp(i kp z)/(k0+kp)) ]

import numpy as np
import S4
import matplotlib.pyplot as plt

S = S4.New(Lattice=((1, 0),(0, 1)), NumBasis=1)
f = 0.4
S.SetFrequency(f)
eps  = 10
epsp = 3

S.SetMaterial(Name = 'Dielectric', Epsilon = (
    (eps + 0.01j, 0 + eps*1j, 0 + 0j), 
    (0 + -eps*1j, eps + 0j, 0 + 0j), 
    (0 + 0j, 0 + 0j, eps + 0j)))

S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Stuff', Thickness = 0, Material = 'Dielectric')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0.0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
                         Order = 0)

k0 = 2*np.pi*f
km = k0*np.sqrt(eps-epsp)
kp = k0*np.sqrt(eps+epsp) 

# UsePolarizationDecomposition
z_space = np.linspace(0, 10, 100)

for z in z_space:
    E, H = S.GetFields(0, 0, z)
    Etx =  (np.cos(km*z)/(k0+km) + np.cos(kp*z)/(k0+kp)) / f
    Ety = -(np.sin(km*z)/(k0+km) - np.sin(kp*z)/(k0+kp)) / f
    print(f'z: {z} Ex: {E[0]} Etx: {Etx} Ey: {E[1]} Ety: {Ety}')

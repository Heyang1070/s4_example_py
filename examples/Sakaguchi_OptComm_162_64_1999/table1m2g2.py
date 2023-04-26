# Duplicates Table 1, M2G2 structure, in
# "Multilayer films composed of periodic magneto-optical and dielectric layers for use as Faraday rotators"
# S. Sakaguchi and N. Sugimoto
# Optics Communications 162, p. 64-70 (1999)

import numpy as np
import S4

for n in range(5, 10):
    S = S4.New(Lattice=((1, 0),(0, 1)), NumBasis=1)

    S.SetMaterial(Name = 'MO', Epsilon = ((4.75 + 0j, 0 + 0.00269j, 0 + 0j), 
                                          (0 + -0.00269j, 4.75 + 0j, 0 + 0j), 
                                          (0 + 0j, 0 + 0j, 4.75 + 0j)))
    
    S.SetMaterial(Name = 'Dielectric', Epsilon = 2.5 + 0.0j)
    S.SetMaterial(Name = 'Vacuum', Epsilon = 1 + 0.0j)

    S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
    S.AddLayer(Name = 'mlayer1', Thickness = 1, Material = 'MO')
    S.AddLayer(Name = 'dlayer1', Thickness = 1.3784, Material = 'Dielectric')

    for i in range(2, n):
        S.AddLayerCopy(Name = 'mlayer' + str(i), Thickness = 1, Layer = 'mlayer1')
        S.AddLayerCopy(Name = 'dlayer' + str(i), Thickness = 1.3784, Layer = 'dlayer1')

    S.AddLayerCopy(Name = 'm2', Thickness = 2, Layer = 'mlayer1')

    for i in range(1, 2*n):
        S.AddLayerCopy(Name = 'dlayer' + str(i+n), Thickness = 1.3784, Layer = 'dlayer1')
        S.AddLayerCopy(Name = 'mlayer' + str(i+n), Thickness = 1, Layer = 'mlayer1')

    S.AddLayerCopy(Name = 'd2', Thickness = 2.7568, Layer = 'dlayer1')

    for i in range(1, n):
        S.AddLayerCopy(Name = 'mlayer' + str(i+3*n), Thickness = 1, Layer = 'mlayer1')
        S.AddLayerCopy(Name = 'mlayer' + str(i+3*n), Thickness = 1.3784, Layer = 'dlayer1')

    S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

    S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
                         Order = 0)
    
    S.SetFrequency(0.25/np.sqrt(4.75))
    forward, backward = S.GetPowerFlux(Layer = 'AirBelow', zOffset = 0)
    E, H = S.GetFields(0, 0, 100)
    Ex = np.sqrt(abs(E[0])**2)
    Ey = np.sqrt(abs(E[1])**2)
    print(f'n:{n} forward:{forward} backward:{backward} angle:{np.pi/180*np.arctan2(Ey, Ex)}')

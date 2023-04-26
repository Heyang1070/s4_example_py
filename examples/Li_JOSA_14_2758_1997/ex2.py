# Example 2 in
# Lifeng Li,
# "New formulation of the Fourier modal method for crossed surface-relief gratings"
# Journal of the Optical Society of America A, Vol. 14, No. 10, p. 2758 (1997)
# This is Fig. 7, curve OCA

import numpy as np
import S4

Sl = []
for i in range(9):
    ng = 41 + 40*i
    Sl.append(S4.New(Lattice=((1, 0),(0.5, 0.5*np.sqrt(3))), NumBasis=ng))

    Sl[i].SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
    Sl[i].SetMaterial(Name = 'Dielectric', Epsilon = 2.56 + 0.0j)

    Sl[i].AddLayer(Name = 'StuffAbove', Thickness = 0, Material = 'Vacuum')
    Sl[i].AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Vacuum')

    Sl[i].SetRegionCircle(
        Layer = 'Slab',
        Material = 'Dielectric',
        Center = (0, 0),
        Radius = 0.25)

    Sl[i].AddLayer(Name = 'StuffBelow', Thickness = 0, Material = 'Dielectric')

    # E polarized along the grating periodicity direction
    Sl[i].SetExcitationPlanewave(IncidenceAngles=(30, 30), 
                            sAmplitude = 0.0 + 0.0j, 
                            pAmplitude = 1 + 0j, 
                            Order = 0)

    # UsePolarizationDecomposition
    Sl[i].SetOptions(Verbosity = 0, 
                LatticeTruncation = 'Circular', 
                DiscretizedEpsilon = False, 
                DiscretizationResolution = 8, 
                PolarizationDecomposition = True, # 打开，默认关闭
                PolarizationBasis = 'Default', 
                LanczosSmoothing = False, 
                SubpixelSmoothing = False, 
                ConserveMemory = False)

    Sl[i].SetFrequency(2.0000001)

    power_inc, _ = Sl[i].GetPowerFlux(Layer = 'StuffAbove', zOffset = 0)
    G = Sl[i].GetBasisSet()
    Gi = 1

    P = Sl[i].GetPowerFluxByOrder(Layer = 'StuffBelow', zOffset = 0)
    print(f'actualg: {ng}, {P[5][0]/power_inc}, {P[5][1]/power_inc}')
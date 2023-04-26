# Extension of Example 1A in
# Lifeng Li,
# "New formulation of the Fourier modal method for crossed surface-relief gratings"
# Journal of the Optical Society of America A, Vol. 14, No. 10, p. 2758 (1997)
# This would be in Fig. 6

import numpy as np
import S4

Sl = []
for i in range(9):
    ng = 41 + 40*i
    Sl.append(S4.New(Lattice=((2.5, 0),(0, 2.5)), NumBasis=ng))

    Sl[i].SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
    Sl[i].SetMaterial(Name = 'Dielectric', Epsilon = 2.25 + 0.0j)

    Sl[i].AddLayer(Name = 'StuffAbove', Thickness = 0, Material = 'Dielectric')
    Sl[i].AddLayer(Name = 'Slab', Thickness = 1.0, Material = 'Vacuum')

    Sl[i].SetRegionRectangle(
        Layer = 'Slab', 
        Material = 'Dielectric',
        Center = (-1.25/2, -1.25/2),
        Angle = 0,
        Halfwidths = (1.25/2, 1.25/2))

    Sl[i].SetRegionRectangle(
        Layer = 'Slab', 
        Material = 'Dielectric', 
        Center = (1.25/2, 1.25/2), 
        Angle = 0, 
        Halfwidths = (1.25/2, 1.25/2))

    Sl[i].AddLayer(Name = 'AirBelow', Thickness = 0, Material = 'Dielectric')

    # E polarized along the grating periodicity direction
    Sl[i].SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                            sAmplitude = 1.0 + 0.0j, 
                            pAmplitude = 0 + 0j, 
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

    Sl[i].SetFrequency(1)

    power_inc, _ = Sl[i].GetPowerFlux(Layer = 'StuffAbove', zOffset = 0)
    P = Sl[i].GetPowerFluxByOrder(Layer = 'AirBelow', zOffset = 0)
    print(f'actualg: {ng}, {P[5][0]/power_inc}')
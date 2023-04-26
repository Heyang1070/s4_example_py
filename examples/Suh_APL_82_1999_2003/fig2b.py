# One curve of Fig. 2b in
# Wonjoo Suh, M. F. Yanik, Olav Solgaard, and Shanhui Fan,
# "Displacement-sensitive photonic crystal structures based on guided resonance in photonic crystal slabs",
# Appl. Phys. Letters, Vol. 82, No. 13, 2003

import numpy as np
import S4

S = S4.New(Lattice=((1, 0),(0, 1)), NumBasis=40)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
S.SetMaterial(Name = 'Silicon', Epsilon = 12.0 + 0.0j)

S.AddLayer(Name = 'AirAbove', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.55, Material = 'Vacuum')

S.SetRegionCircle(
    Layer = 'Slab', 
    Material = 'Vacuum', 
    Center = (0,0), 
    Radius = 0.4)

S.AddLayerCopy(Name = 'Spacer', Thickness =1.1, Layer = 'AirAbove')
S.AddLayerCopy(Name = 'Slab2', Thickness =0.55, Layer = 'Slab')
S.AddLayerCopy(Name = 'AirBelow', Thickness = 0, Layer = 'AirAbove')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 1 + 0.0j, 
                         pAmplitude = 0 + 0j, 
                         Order = 0)

S.SetOptions(Verbosity = 0, 
                 LatticeTruncation = 'Circular', 
                 DiscretizedEpsilon = False, 
                 DiscretizationResolution = 8, 
                 PolarizationDecomposition = True, # 打开，默认关闭
                 PolarizationBasis = 'Default', 
                 LanczosSmoothing = False, 
                 SubpixelSmoothing = False, 
                 ConserveMemory = False)


freq_space = np.linspace(0.49, 0.6, 110)
for freq in freq_space:
    S.SetFrequency(freq)

    forward, _ = S.GetPowerFlux(Layer = 'AirBelow', zOffset = 0)
    print(f'freq: {freq} forward: {forward}')

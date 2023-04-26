# Fig. 4 in
# Quasi-guided modes and optical properties of photonic crystal slabs
# S.G. Tikhodeev, A.L. Yablonskii, E.A. Muljarov, N.A. Gippius, and T. Ishihara
# Phys. Rev. B 66, 45102 (2002)

import numpy as np
import S4

S = S4.New(Lattice=((0.68, 0),(0, 0.68)), NumBasis=100)

S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)
S.SetMaterial(Name = 'Active', Epsilon = 3.79 + 0.0j)
S.SetMaterial(Name = 'Quartz', Epsilon = 2.132 + 0.0j)

S.AddLayer(Name = 'Front', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.12, Material = 'Quartz')

S.SetRegionRectangle(
    Layer = 'Slab', 
    Material = 'Active', 
    Center = (0, 0), 
    Angle = 0, 
    Halfwidths = (0.4*0.68, 0.4*0.68))

S.AddLayer(Name = 'Back', Thickness = 0, Material = 'Quartz')

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

Sa = []
npar = 3
for i in range(npar):
    Sa.append(S.Clone())

step = 0.002
ev_space = np.linspace(1, 2.602, 267)
for ev in ev_space:
    for i in range(npar):
        f = 0.8065548889615557*(ev + i*step)
        Sa[i].SetFrequency(f)

    for i in range(npar):
        forward, backward = S.GetPowerFlux(Layer = 'Back', zOffset = 0)
        print(f'ev: {ev + i*step} , forward : {forward}, backward: {backward}')

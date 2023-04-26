# Fig. 2b in
# A. Christ, T. Zentgraf, J. Kuhl, S. G. Tikhodeev, N. A. Gippius, and H. Giessen
# "Optical properties of planar metallic photonic crystal structures: Experiment and theory"
# Physical Review B 70, 125113 (2004)

import numpy as np
import S4
import matplotlib.pyplot as plt

S = S4.New(Lattice=((0.5, 0),(0, 0)), NumBasis=49)
S.SetMaterial(Name = 'ITO', Epsilon = 2.0 + 0.0j)
S.SetMaterial(Name = "Quartz", Epsilon = 2.14 + 0j)
S.SetMaterial(Name = "Vacuum", Epsilon = 1 + 0j)
S.SetMaterial(Name = "Gold", Epsilon = -5 + 0j)

S.AddLayer(Name = 'Front', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'Grating', Thickness = 0.015, Material = 'Vacuum')
S.AddLayer(Name = 'Slab', Thickness = 0.5, Material = 'Silicon')
S.SetRegionRectangle(Layer = 'Grating', Material = 'Gold', 
                  Center = (0, 0), 
                  Angle = 0, 
                  Halfwidths = (0.05, 0))
S.AddLayer(Name = 'Spacer', Thickness = 0.015, Material = 'ITO')
S.AddLayer(Name = 'Back', Thickness = 0, Material = 'Quartz')

# E polarized along the grating periodicity direction
S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0.0 + 0.0j, 
                         pAmplitude = 1 + 0j, 
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
ev_space = np.linspace(1.5, 2.4, int(0.9/(step*npar)))
for ev in ev_space:
    for i in range(npar):
        iev = ev + i*step
        f = 0.8065548889615557 * iev
        l2 = 1/(f*f)
        Sa[i].SetMaterial(Name = 'Gold', Epsilon =  -5 + 10.0j)
        Sa[i].SetMaterial(Name = 'ITO', 
                          Epsilon = (1 + 1.81302*12/(12 - 0.07597)) + 0.0j)
        Sa[i].SetFrequency(f)
    
    for j in range(npar):
        iev = ev + j*step
        t = Sa[j].GetPowerFlux(Layer = 'Back', zOffset = 0)
        print(iev, -np.log(t))



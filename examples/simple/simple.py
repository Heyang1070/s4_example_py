import numpy as np
import matplotlib.pyplot as plt
import S4

# a simple planewave travelling through vacuum

S = S4.New(Lattice=((1, 0),(0, 1)), NumBasis=1)
S.SetMaterial(Name = 'Vacuum', Epsilon = 1.0 + 0.0j)

S.AddLayer(Name = 'Front', Thickness = 0, Material = 'Vacuum')
S.AddLayerCopy(Name = 'Back', Thickness = 0, Layer = 'Front')

S.SetExcitationPlanewave(IncidenceAngles=(0, 0), 
                         sAmplitude = 0.0 + 0.0j, 
                         pAmplitude = 1.0 + 0j, 
                         Order = 1)

S.SetFrequency(0.5)

# -2 <= z <= 2
E, H = S.GetFields(0, 1, 0)
print(f'E = {E} \n H = {H}')
	
from pymatgen.core.structure import Structure
import pandas as pd
import os
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.composition import (ElementProperty, OxidationStates, 
AtomicOrbitals, BandCenter, ElectronegativityDiff) #Composition Features
from matminer.featurizers.structure import (DensityFeatures, RadialDistributionFunction, 
PartialRadialDistributionFunction, ElectronicRadialDistributionFunction, CoulombMatrix) #Structure Features
import numpy as np

#Grabs all CIF files in a directory
CIFfiles = []  
directoryname = '../matDiscovery/examples/' #The directory it looks in
allfiles = os.listdir(directoryname)
for i in allfiles:
    if os.path.splitext(i)[-1] == '.cif':
        CIFfiles.append(i) #List of CIF files

#Creates a list of pymatgen.structure objects and a name of each structure
structlist = []
namelist = []
structs = []
namecolumns = ['structure']
for i in CIFfiles:
    structlist.append([Structure.from_file(directoryname+i)]) #Converts CIF to pymatgen structure object
    namelist.append(os.path.splitext(i)[0]) #Collects all the structure names
    structs.append(Structure.from_file(directoryname+i))
#Creates Pandas dataframe with data being a list of structures and the row name being the structure name
dftest = pd.DataFrame(data = structlist, index = namelist, columns=namecolumns) 

p = PartialRadialDistributionFunction()
p.fit(np.asarray(structs))

c = CoulombMatrix()
c.fit(np.asarray(structs))

erdf = ElectronicRadialDistributionFunction()
erdf.cutoff = 10 #longest diagonal of lattice...I picked a number semi-arbitrarily

#Featurizes the structures
featurizer = MultipleFeaturizer([ElementProperty.from_preset('magpie'), OxidationStates(), 
                                 AtomicOrbitals(), BandCenter(), ElectronegativityDiff(), DensityFeatures(), 
                                 RadialDistributionFunction(), p, c, erdf])

r=(featurizer.featurize_many(dftest, ['structure'])) #Featurizes entire Pandas Dataframe  
#Yay it runs!

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
namecolumns = ['structure']
for i in CIFfiles:
    structlist.append([Structure.from_file(directoryname+i)]) #Converts CIF to pymatgen structure object
    namelist.append(os.path.splitext(i)[0]) #Collects all the structure names

#Creates Pandas dataframe with data being a list of structures and the row name being the structure name
dftest = pd.DataFrame(data = structlist, index = namelist,columns=namecolumns) 

#unsure if running a particular instance of a class will mess anything up in MultipleFeaturizer()
p = PartialRadialDistributionFunction()
p.fit(np.asarray(structlist)[0])

c = CoulombMatrix()
c.fit(np.asarray(structlist)[0])

erdf = ElectronicRadialDistributionFunction()
erdf.cutoff = 3 #longest diagonal of lattice...I picked a number semi-arbitrarily

#Featurizes the structures
featurizer = MultipleFeaturizer([ElementProperty.from_preset('magpie'), OxidationStates(), 
                                 AtomicOrbitals(), BandCenter(), ElectronegativityDiff(), DensityFeatures(), 
                                 RadialDistributionFunction(), p, c, erdf])

r=(featurizer.featurize_dataframe(dftest, ['structure'])) #Featurizes entire Pandas Dataframe 

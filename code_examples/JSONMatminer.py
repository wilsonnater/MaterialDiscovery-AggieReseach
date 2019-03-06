'''
This code isn't correct yet, I'm getting an error in my for loop.
Also, I don't think I've set up my json files correctly, because theoretically
each json file contains multiple structures, and this code assumes each file contains
exactly one structure
'''

from pymatgen.core.structure import Structure
import pandas as pd
import os, sys
import json
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.composition import (ElementProperty, OxidationStates, 
AtomicOrbitals, BandCenter, ElectronegativityDiff) #Composition Features
from matminer.featurizers.structure import (DensityFeatures, RadialDistributionFunction, 
PartialRadialDistributionFunction, ElectronicRadialDistributionFunction, CoulombMatrix) #Structure Features

module_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(module_dir, "..", "utils", "data_files")


#Grabs all json files in a directory
JSONfiles = []  
directoryname = '../matDiscovery/' #The directory it looks in 
allfiles = os.listdir(directoryname)
for i in allfiles:
    if os.path.splitext(i)[-1] == '.json':
        JSONfiles.append(i) #List of json files

#Creates a list of pymatgen.structure objects and a name of each structure
structlist = []
namelist = []
namecolumns = ['structure']

for i in JSONfiles:
        structlist.append([Structure.from_file(directoryname+i)]) #Converts JSON to pymatgen structure object
        namelist.append(os.path.splitext(i)[0]) #Collects all the structure names
#ERROR: list indices must be integers or slices, not str


#Creates Pandas dataframe with data being a list of structures and the row name being the structure name
dftest = pd.DataFrame(data = structlist, index = namelist, columns=namecolumns) 

#Featurizes the structures
featurizer = MultipleFeaturizer([ElementProperty("pymatgen", ["X", "row", "group", "block", "atomic_mass", "atomic_radius"],
["minimum", "maximum", "range", "mean", "std_dev"]), OxidationStates(), AtomicOrbitals(), 
BandCenter(), ElectronegativityDiff(), DensityFeatures(), RadialDistributionFunction(), 
PartialRadialDistributionFunction(), ElectronicRadialDistributionFunction(), CoulombMatrix()]) 

r=(featurizer.featurize_dataframe(dftest,['structure'])) #Featurizes entire Pands Dataframe 



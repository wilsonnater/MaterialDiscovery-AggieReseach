from pymatgen.core.structure import IStructure
import pandas as pd
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.composition import ElementProperty #Composition Feature
from matminer.featurizers.structure import (StructuralHeterogeneity, StructureComposition) #Structure features

#Grabs all CIF files in a directory
CIFfiles = []  
directoryname = '../examples/' #The directory it looks in
allfiles = os.listdir(directoryname)
for i in allfiles:
    if os.path.splitext(i)[-1] == '.cif':
        CIFfiles.append(i) #List of CIF files

#Creates a list of pymatgen.structure objects and a name of each structure
structlist = []
namelist = []
namecolumns = ['structure']
for i in CIFfiles:
    structlist.append([IStructure.from_file(directoryname+i)]) #Converts CIF to pymatgen structure object
    namelist.append(os.path.splitext(i)[0]) #Collects all the structure names


#Creates Pandas dataframe with data being a list of structures and the row name being the structure name
dftest = pd.DataFrame(data = structlist, index = namelist,columns=namecolumns) 


#Featurizes the structures
featurizer = MultipleFeaturizer([StructuralHeterogeneity(), #sets the featurizers that are going to be used
    StructureComposition(ElementProperty.from_preset('magpie'))]) # This one also collects the composition from the structures
#more featurizers can be added

r=(featurizer.featurize_dataframe(dftest,['structure'])) #Featurizes entire Pands Dataframe 


##Code grabs CIF files and then puts them into
##Pymatgen structure object using built in pymatgen
##tool. Then checks if number of sites is between 
##2 and 10 and if the strcutre includes any atoms that
##it was told to avoid. Is made for linux operating system

from pymatgen.core import structure
import numpy as np
import os
import shutil
rootdir = 'nate_oqmd_data'

extensions = ('.cif')
finaldir = 'sub_oqmd_data'
#atoms to avoid
avoid = np.append(np.append(np.array([1 , 2, 10, 18,36, 54, 86]),np.arange(57,72)),np.arange(84,113))

for subdir, dirs, files in os.walk(rootdir):
    for dfile in files:
        ext = os.path.splitext(dfile)[-1].lower()
        top = os.path.splitext(dfile)[0]
        if ext in extensions:
            go = True
            ciffile = os.path.join(subdir, dfile)
            struct=structure.IStructure.from_file(ciffile) #Creates structure object from CIF
            if 2<struct.num_sites<10:   #Checks if number of sites is between 2 and 10
                npavoid = np.unique(np.array(struct.atomic_numbers)) #gets unique atomic numbers
                for i in npavoid: #loops over all unique atomic numbers
                    if i in avoid:   #the atomic number is in avoid sets go to flase
                        go = False
            else:
                go=False
            if go:
                jsonf=(top+'.json')
                shutil.copy(ciffile,os.path.join(finaldir, dfile)) ##copies CIF
                shutil.copy(os.path.join(subdir, jsonf),os.path.join(finaldir, jsonf)) ##copies JSON

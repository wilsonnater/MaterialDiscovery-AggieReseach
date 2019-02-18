from pymatgen.core import structure
import numpy as np
import os
import shutil
rootdir = 'nate_oqmd_data'

extensions = ('.cif')
finaldir = 'sub_oqmd_data'

avoid = np.append(np.append(np.array([1 , 2, 10, 18,36, 54, 86]),np.arange(57,72)),np.arange(84,113))

for subdir, dirs, files in os.walk(rootdir):
    for dfile in files:
        ext = os.path.splitext(dfile)[-1].lower()
        top = os.path.splitext(dfile)[0]
        if ext in extensions:
            go = True
            ciffile = os.path.join(subdir, dfile)
            struct=structure.IStructure.from_file(ciffile)
            if 2<struct.num_sites<10:
                npavoid = np.unique(np.array(struct.atomic_numbers))
                for i in npavoid:
                    if i in avoid:
                        go = False
            else:
                go=False
            if go:
                jsonf=(top+'.json')
                shutil.copy(ciffile,os.path.join(finaldir, dfile))
                shutil.copy(os.path.join(subdir, jsonf),os.path.join(finaldir, jsonf))

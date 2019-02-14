#gets data from aflow and write to json file
#need to write to cif file instead of json?
import numpy
from aflow import *
import json

result = search(batch_size=10).exclude(K.species == "H").exclude(K.species == "He").exclude(K.species == "Ne"
).exclude(K.species == "Ar").exclude(K.species == "Kr").exclude(K.species == "Xe").exclude(K.species == "La"
).exclude(K.species == "Ce").exclude(K.species == "Pr").exclude(K.species == "Nd").exclude(K.species == "Pm"
).exclude(K.species == "Sm").exclude(K.species == "Eu").exclude(K.species == "Gd").exclude(K.species == "Dy"
).exclude(K.species == "Ho").exclude(K.species == "Er").exclude(K.species == "Tm").exclude(K.species == "Tb"
).exclude(K.species == "Lu").exclude(K.species == "Ac").exclude(K.species == "Th").exclude(K.species == "Pa"
).exclude(K.species == "U").exclude(K.species == "Np").exclude(K.species == "Pu").exclude(K.species == "Am"
).exclude(K.species == "Cm").exclude(K.species == "Bk").exclude(K.species == "Cf").exclude(K.species == "Es"
).exclude(K.species == "Fm").exclude(K.species == "Md").exclude(K.species == "No").exclude(K.species == "Lr"
).exclude(K.species == "Po").exclude(K.species == "At").exclude(K.species == "Rn").exclude(K.species == "Fr"
).exclude(K.species == "Ra").exclude(K.species == "Rf").exclude(K.species == "Db").exclude(K.species == "Sg"
).exclude(K.species == "Bh").exclude(K.species == "Hs").exclude(K.species == "Mt").exclude(K.species == "Ds"
).exclude(K.species == "Rg").exclude(K.species == "Cn").select(K.compound)

for entry in result:
    
    with open("aflowdata.json", "a") as write_file:
        ##input to ML algorithm
        name = entry.compound
        lattice = entry.geometry
        ident = entry.auid
            
        na = entry.natoms
        ratio = entry.stoich
        position = entry.positions_fractional

        ##output that ML predicts
        forceMatrix = entry.forces
        stress = entry.stress_tensor
               
        import numpy as nm
        #if statements which tests if structures are present 
        if isinstance(lattice, numpy.ndarray):
            tup =  nm.shape(lattice)
            ncols = tup[0]
            geo = [ncols]
                
            for i in range(ncols):
                geo.append(lattice[i])
        else:
            geo = []

        if isinstance(forceMatrix, numpy.ndarray):
            tup =  nm.shape(forceMatrix)
            ncols = tup[1]
            nrows = tup[0]
            fm = [nrows, ncols]
                
            for i in range(nrows):
                for j in range(ncols):
                    fm.append(forceMatrix[i][j])
        else:
            fm = []

        if isinstance(stress, numpy.ndarray):
            tup =  nm.shape(stress)
            ncols = tup[0]
            st = [ncols]
                
            for i in range(ncols):
                st.append(stress[i])
        else:
            st = []

        if isinstance(position, numpy.ndarray):
            tup =  nm.shape(position)
            ncols = tup[0]
            pos = [ncols]
                
            for i in range(ncols):
                pos.append(position[i])
        else:
            pos = []

        if isinstance(ratio, numpy.ndarray):
            tup =  nm.shape(ratio)
            ncols = tup[0]
            r = [ncols]
                
            for i in range(ncols):
                r.append(ratio[i])
        else:
            r = []

        item = {
        "name": name, "lattice": geo,
        "na": na, "ident": ident, "ratio": r,
        "position": pos, "forceMatrix": fm,
        "stress": st
        }
        #if item has everything, go ahead and write it, else, scrap
        if (geo and fm and r and pos and st):
            json.dump(item, write_file, indent = 4)
        

#NEED TO DO:
#install matminer 

from pymatgen.ext.matproj import MPRester ##Pymatgen module will have to be installed
import json

##Querys the materialsproject database. For MPRester you shoud 
##get your own API key (MPRester('APIkey')) from materials project
with MPRester('y6hicvzKBaLRWuG8') as m:
    ##Querys materials project for all strucutres with 2<= sites <=3 (all structures with 2 or 3 atomic sites)
    ##also does n0t download any structures that contain Cl or Al
    ##It gets the strucutre and task_id from material project
    results = m.query(criteria={"nsites":{"$gte":2,"$lte":3},"elements":{"$nin":["Cl","Al"]}},properties=['structure','task_id','full_formula'])

##Writes data into json file
##Much of this is using pymatgen stuff indirectly
data={}
for i in range(0,4):
    struct = results[i]['structure'] ##PYmatgen Structure object
    Name = results[i]['task_id']  ##Change 1: I changed the first branching of the data to be task_id instead of chemical formula
    ##This change is becuase a chemcial formula is not a unique identifier and so there can be repeats that cause trouble
    NS = struct.num_sites
    atoms = struct.sites
    matrix = struct.lattice.matrix ##From pymatgen get the lattice in matrix form
    data[Name]={}
    data[Name]['lattice'] = matrix.tolist()  
    data[Name]['atoms'] = []
    for i in range(NS):
        atom = atoms[i]
        data[Name]['atoms'].append([atom.specie.symbol,atom.frac_coords.tolist()]) ##Change 2: I made it so that the atomic species (atomic symbol)
		## is outside of the fractional coordinates. This is for ease of writing/accessing it and that normally the species and position(all 3 coordinates together)
		##are two seperate pieces of information

with open("pymatdata.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)


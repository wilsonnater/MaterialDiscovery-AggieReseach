#Creates a list of pymatgen.structure objects and a name from each heterostructure
structlist = []
for i in posfiles:
    structlist.append([Structure.from_file(pathtodir+i)])
#adds oxidation state by guessing through pymatgen
for i in range(len(structlist)):
    structlist[i][0].add_oxidation_state_by_guess()
namecolumns = ['structure']

#Creates Pandas dataframe with data being a list of structures and the row name being the structure name
dftest = pd.DataFrame(data = structlist, index = posfiles,columns=namecolumns) 

#Featurizes the structures
#Creates the Featurizers and sets any required inputs for them
featurizer = MultipleFeaturizer([GlobalSymmetryFeatures(),ElectronicRadialDistributionFunction(cutoff=7.5),
    SiteStatsFingerprint(AGNIFingerprints(directions=(None,'x', 'y'))),SiteStatsFingerprint(OPSiteFingerprint()),
    SiteStatsFingerprint.from_preset("CoordinationNumber_ward-prb-2017"),SiteStatsFingerprint(GaussianSymmFunc()),
    SiteStatsFingerprint(EwaldSiteEnergy(accuracy=3)),DensityFeatures(),
    SiteStatsFingerprint(GeneralizedRadialDistributionFunction.from_preset('gaussian')),
    SiteStatsFingerprint(LocalPropertyDifference(data_source=MagpieData(),
    properties=["Number", "MendeleevNumber", "AtomicWeight","MeltingT", "Column", "Row", "CovalentRadius",
    "Electronegativity", "NsValence", "NpValence","NdValence", "NfValence", "NValence", "NsUnfilled",
    "NpUnfilled", "NdUnfilled", "NfUnfilled", "NUnfilled", "GSvolume_pa", "GSbandgap","GSmagmom"])),
    SiteStatsFingerprint(SiteElementalProperty.from_preset("seko-prb-2017")),EwaldEnergy(),
    StructuralHeterogeneity(),ChemicalOrdering(),StructureComposition(ElementProperty.from_preset('magpie')),
    StructureComposition(AtomicOrbitals()),StructureComposition(BandCenter()),StructureComposition(ElectronegativityDiff()),
    StructureComposition(ElectronAffinity()),StructureComposition(Stoichiometry()),
    StructureComposition(ValenceOrbital()),StructureComposition(IonProperty()),StructureComposition(Miedema()),
    StructureComposition(YangSolidSolution())])

#Featurization had to be run in pieces because of the size of the data
r=(featurizer.featurize_dataframe(dftest,['structure'],ignore_errors=True)) #Featurizes entire Pands Dataframe 

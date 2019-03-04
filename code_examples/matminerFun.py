import matminer
import pymatgen
import pandas

from matminer.data_retrieval.retrieve_MP import MPDataRetrieval

df_mp = MPDataRetrieval("y6hicvzKBaLRWuG8").get_dataframe(criteria={"task_id":{"$in":["mp-22862"]}},
 properties=["structure"])
print(type(df_mp)) #pandas dataframe
print(df_mp.iloc[0]) #outputs the following: structure    [[0. 0. 0.] Na, [2.32362417 1.64305041 4.02463...
                     #                       Name: mp-22862, dtype: object
# Needed to go one level deeper in df_mp
print(df_mp.iloc[0][0])
# If you look at the type of file that is it is pymatgen.structure.Structure object
print(type(df_mp.iloc[0][0]))
#this is a dataformat we can create

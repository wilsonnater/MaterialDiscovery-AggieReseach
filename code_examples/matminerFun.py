import matminer
import pymatgen
import pandas

from matminer.data_retrieval.retrieve_MP import MPDataRetrieval

df_mp = MPDataRetrieval("y6hicvzKBaLRWuG8").get_dataframe(criteria={"task_id":{"$in":["mp-22862"]}},
 properties=["structure"])
print(type(df_mp)) #pandas dataframe
print(df_mp.iloc[0]) #outputs the following: structure    [[0. 0. 0.] Na, [2.32362417 1.64305041 4.02463...
                     #                       Name: mp-22862, dtype: object


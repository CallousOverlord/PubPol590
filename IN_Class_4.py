from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\Kyle\Documents\NSOE_semester_4\Big_Data\practice"
git_dir = "C:\Users\Kyle\Documents\GitHub\PubPol590"
csv_file = "small_data_w_missing_duplicated.csv"
csv2 = "sample_assignments.csv"


#import data

df1 = pd.read_csv(os.path.join(main_dir, csv_file), na_values = ['-', 'NA'])
df2 = pd.read_csv(os.path.join(main_dir, csv2))

#CLEAN DATA-----
#clean df1
df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(['panid', 'date'], take_last = True)

#clean df2
df2[[0,1]]
df2 = df2[[0,1]]


#Copy DataFrames--------------------------------
df3 = df2 #creats a link/reference (alters df2 DOES AFFECT df3)
df4 = df2.copy() #creates a copy (altering df2 does not affect df4

#REPLACEING DATA----------------------------------
df2.group.replace(['T', 'C'], [1,0])
df2.group = df2.group.replace(['T', 'C'], [1,0])

#MERGING -----------------------------------
pd.merge(df1,df2) # 'many-to-one' merge using the intersection. Automatically finds the keys it has in common
dfmerg = pd.merge(df1,df2, on = ['panid']) #specifies key what to merge on
dfmerg = pd.merge(df1,df2, on = ['panid'], how = 'inner')
dfmerg = pd.merge(df1,df2, on = ['panid'], how = 'outer')
df5 = pd.merge(df1,df2, on = ['panid']) #note that merge creates a new object


#STACKING AND BINDING (ROW BINDS AND COLUMN BINDS)
df2
df4
## 'row bind'
pd.concat([df2,df4]) #default it to rowbind
pd.concat([df2,df4], axis = 0) #same as above
pd.concat([df2,df4], axis = 0, ignore_index = True) #resets index

#column bind
pd.concat([df2, df4], axis =1)


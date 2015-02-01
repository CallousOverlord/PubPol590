from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\Kyle\Documents\NSOE_semester_4\Big_Data\practice"
git_dir = "C:\Users\Kyle\Documents\GitHub\PubPol590"
csv_file = "small_data_w_missing_duplicated.csv"

##Create the Dataframes
df1 = pd.read_csv(os.path.join(main_dir, csv_file))
df1

#finding missing values
missing = ['.', 'NA', '-', '', 'NULL', '-']
df1 = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)
df1.head()

#Drop duplicates----------------------------------------------------------------
df1.duplicated()
df1.drop_duplicates()
df1 = df1.drop_duplicates()

#Pulling rows where consump is missing data-------------------------------------
df1['consump'].isnull() #ids missing data in consump column in edited df1
missing = df1['consump'].isnull()
df1[missing] #shows only the rows that are missing consump data

#-------------------------------Working on this---------------------------------

# df1 = df1.dropna() #drops any row that is missing any data


#panid and data duplicates?
df1.duplicated(['panid', 'date'])
pdrows = df1.duplicated(['panid', 'date'])
df1[pdrows] #shows rows that are not duplicated
df1 = df1.drop_duplicates(['panid', 'date']) #removes duplicates of panid and date from db1

## Mean of variable consump
print df1['consump'].mean()




from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#Kyle Thomas test file for class 2

# IMPORTING DATA -------------------------------------------------------

## ASSIGNING FILE PATHS

main_dir = "C:\Users\Kyle\Documents\GitHub\PubPol590\class_2_demo"
csv_file = "\data\sample_data_clean.csv"
txt_file = "\data\sample_data_clean.txt"

main_dir + csv_file
main_dir + txt_file

#read_csv and read_table
df = pd.read_csv(main_dir + csv_file)
df2 = pd.read_table(main_dir + txt_file)

# check object type
type(df)

# exploring dataframe ---------------------------------------------------
list(df) # gets names of dataframe

## extracting colums/series of data ---------------------------------------
c = df.consump
c2 = df['consump']

type(c)

#BOOLEAN OPERATORS ----------------------------------------------------------
c == c2 #equal
c >c2 #greater
c >= c2
c != c2 #not equal

#other boolean operators <, <=, !=

## ROW EXTRACTION --------------------------------------------------

# Row slicing
df[5:10] #df[m:n] yeilds rows m to n-1
df[0:10]
df[:10]
df[0:10] == df[:10]
df[10:11]

#slicing from series
c[5:10] #same as df.consump[5:10]

## extraction by boolean indexing
df.panid == 4
df[df.panid == 4] #extract subset of df where panid == 4

df[df.consump > 2]

df.panid[df.panid > 2]


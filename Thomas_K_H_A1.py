from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "C:\Users\Kyle\documents\GitHub\PubPol590\class_2_demo"
txt_file = "\data\File1_small.txt"


#import data--------------------------------------------------------------------
df = pd.read_table(main_dir + txt_file, sep = "\s")

#verifying data-----------------------------------------------------------------
list(df)

#slicing rows 60 to 99----------------------------------------------------------

df[60:100]
rws = df[60:100]

# rows with electricty consumption greater than 30 kWh--------------------------

df[df.kwh > 30]
gtr30 = df[df.kwh > 30]






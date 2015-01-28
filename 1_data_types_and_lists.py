from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


#code goes in GitHub directory, and data goes in main directory-----------------
main_dir = "C:\Users\Kyle\Desktop\data"
git_dir = "C:\Users\Kyle\Documents\GitHub\PubPol590"
csv_file = "sample_data_clean.csv"
csv_file_bad = "/sample_data_clean.csv"

# OS MODULE---------------------------------------------------------------------
df = pd.read_csv(os.path.join(main_dir, csv_file))
# this code should not work  df = pd.read_csv(os.path.join(main_dir, csv_file_bad)

#PYTHON DATA TYPES--------------------------------------------------------------
## strings
str1 = "hello, computer"
str2 = 'hello human'
str3 = u'eep'

type(str1) #type str
type(str2) #
type(str3)

#numeric
int1 = 10
float1 = 20.56
long1 = 3251878465468879879846587987984564987987987

##logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)



#CREATING LISTS AND TUPLES------------------------------------------------------
##list can be changed, tuples cannot, we will be using lists for the most part--

list1 = []

list2 = [1,2,3]
list2[2]

list2[2] = 5

#tuples, can't change
tupl1 = (8,3,19)

##convert
list2 = list(tupl1)
tup2 = tuple(list2)

## lists can be appended and extended
list2.append([3,30]) #adds a list
list2 = [8,3,90]
list2.extend([6,88])
len(list2)
list4 = range(5,10) #range(n,m) gives a list from n to m-1
list5 = range(5) #starting from zero to m-1

#converting lists to series and dataframes

s1 = Series(list4)
s2 = Series(list5)

## lists to dataframes
df1 = 





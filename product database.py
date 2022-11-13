# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:50:27 2022

@author: biruk
"""
from pathlib import Path
import pandas as pd
import os
import glob
import sys


input_dir = Path.cwd() / r"C:\Users\biruk\Documents\UN\TiVA\Machine learning\Database" # insert here the file path of the directory on your machine
# on windows computer insert the path like this r"C:\Users\your\file\path
# path of the folder

#looping over folders and files in directory
#for root, dirs, files in os.walk(".", topdown=True):
 #  for name in files:
  #    print(os.path.join(root, name))
   #for name in dirs:
    #  print(os.path.join(root, name))
# glob = specific folder
# rglob = including subfolder
#files = list(input_dir.rglob("*.xlsx"))
#files

import pandas as pd  # pip install pandas

# Store dataframes in a list
parts = []
for path in list(input_dir.rglob("*.xlsx")):
    part = pd.read_excel(path)
    parts.append(part)
    
# Concatenate dataframes
df = pd.concat(parts)

# Save merged dataframe to output directory
output_dir = Path.cwd() / "MasterFile"
output_dir.mkdir(exist_ok=True)
df.to_excel(output_dir / "masterfile.xlsx", index=False)

df.head()

df.drop('Unnamed: 0', axis=1, inplace=True)

# Show the data frame
df.fillna(0,inplace=True)
df.head()

# Replacing out any NAN value with Zero
df[df.isnull().any(axis=1)]

df2 = df[df['ProductDescription'].str.contains('peche', na = False)]
df2

## Count number of time code appears
df2["ProductCode"].value_counts()

df.to_excel('cleaned.xlsx', index = False)

##import new file to match
new_country = list(input_dir.rglob("GHA_products.xlsx"))
country = pd.read_excel("C:\\Users\\biruk\\Documents\\UN\\TiVA\\Machine learning\\Database\\GHA_products.xlsx")

##loop through product descriptions and match to closest code from database
for ProductDescription in country.iteritems():
    print('Column Name : ', ProductDescription)


### balancing matrix
from scipy import linalg
import numpy as np
x = np.array([[1,2,7], [9,1,1], [1,2,10*np.pi]])

y, permscale = linalg.matrix_balance(x)    
np.abs(x).sum(axis=0) / np.abs(x).sum(axis=1)        
np.abs(y).sum(axis=0) / np.abs(y).sum(axis=1)


permscale  

tv = pd.read_excel("C:\\Users\\biruk\\Documents\\UN\\TiVA\\Database\\tv3.xlsx")
tv = tv()
x = tv
y, balanced = linalg.matrix_balance(tv)

from sinkhorn_knopp import sinkhorn_knopp as skp
sk = skp.SinkhornKnopp()
P_ds = sk.fit(tv)
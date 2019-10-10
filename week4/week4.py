#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt 
import numpy as np


# read vec file
# extracting column 2 and 3 
# convert to numbers and store (list)
# plot these columns for each line

listx = []
listy = []

for line in open(sys.argv[1]):
    column = line.rstrip("\t").split()
    listx.append(float(column[2]))
    listy.append(float(column[3]))
#print(listx) 

# intitate figure
fig,ax = plt.subplots()
plt.scatter(listx,listy)
plt.xlabel('component1')
plt.ylabel('component2')
fig.savefig('PCA')

         


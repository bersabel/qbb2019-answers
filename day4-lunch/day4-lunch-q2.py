#!/usr/bin/env python3

"""
Usage :.//00-scat
"""



import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t" , index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t" , index_col="t_name")

fpkm = { name1 : ctab1.loc[:,"FPKM"],
         name2 : ctab2.loc[:,"FPKM"]}        

df = pd.DataFrame( fpkm )

goi = np.log2(df.loc[:,name1 ] +1)
goi2 = np.log2(df.loc[:,name2 ] +1)

print(df)

# exons = []
# lengths = []
# myexons = np.log2(exons)
# mylengths = np.log2(lengths)
#
# for i, line in enumerate( open(sys.argv[1])):
#     if i == 0:
#         continue
#     fields = line.rstrip("\n").split("\t")
#     exons.append( int(fields[6]) )
#     lengths.append ( int(fields[7]))
#
polyfit = np.polyfit(goi, goi2, 1) 
poly1d = np.poly1d(polyfit)
xv = np.linspace(0, 14, 100)
fig, ax = plt.subplots()
ax.scatter( x= goi, y= goi2, alpha = 0.5, color="red")
# ax.plot( [0,40], [0,20000], color="red")
ax.set_title("scatterplot")
ax.set_xlabel("log2 FPKMS {}".format(name1))
ax.set_ylabel("log2 FPKMS {}".format(name2))

ax.plot( xv,poly1d(xv) )
fig.savefig("sample1-v-sample2.png")
plt.close( fig )



#
# my_data = np.log2( fpkms )
# ax.hist( my_data, bins = 100 , density = True )


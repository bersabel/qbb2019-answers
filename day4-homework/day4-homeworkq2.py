#!/usr/bin/env python3
"""
boxplot all transcripts for a given gene
"""




import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv( fpkm_file , index_col="t_name")

# for i, line in enumerate( open(metadata)):
#     if i == 0:
#         continue
# fields = line.rstrip("\n").split(",")
goi = df.loc[:,"gene_name"] == gene_name
# fpkms = df.drop(fields[10:17])
fpkms1 = df.drop(df.columns[list(range(9,17))],axis=1)
fpkms1 = fpkms1.drop(columns="gene_name")
# print(fpkms)
# goi2 = df.loc[:,"gene_name"] == gene_name
fpkms2 = df.drop(df.columns[list(range(1,9))],axis=1)
fpkms2 = fpkms2.drop(columns="gene_name")

# print( fpkms.loc[goi,:] )
# print(pkms)



fig, (ax1,ax2) = plt.subplots(2)
ax1.boxplot( fpkms1.loc[goi,:].T)
ax2.boxplot( fpkms2.loc[goi,:].T)

ax1.set_title("Female")
ax1.set_xlabel("")
ax1.set_xticks([1, 2, 3,4,5,6,7,8])
ax1.set_xticklabels(['Female_10', 'Female_11', 'Female_12','Female_13','Female_14A','Female_14B','Female_14C','Female_14D'], rotation = 45)
# plt.xticks([1, 2, 3,4,5,6,7,8], ['Female_10', 'Female_11', 'Female_12','Female_13','Female_14A','Female_14B','Female_14C','Female_14D'])
ax1.set_ylabel("expression")
ax2.set_title("Male")
plt.xticks([1, 2, 3,4,5,6,7,8], ['male_10', 'male_11', 'male_12','male_13','male_14A','male_14B','male_14C','male_14D'], rotation = 45)
ax2.set_xlabel("")
ax2.set_ylabel("expression")
plt.subplots_adjust(hspace = 0.7)
fig.savefig( "boxplot.png")
plt.close( fig )







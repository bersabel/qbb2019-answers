#!/usr/bin/env python3

"""
./day4-lunch-q2.py ../results/stringtie/SRR072893/t_data.ctab ../results/stringtie/SRR072894/t_data.ctab
"""


import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name1 = sys.argv[1].split(os.sep)[-2] 
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name") 

name2 = sys.argv[2].split(os.sep)[-2] 
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm = {name1: ctab1.loc[:,"FPKM"], 
        name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm) 


fpkmss1 = np.log2(df.loc[:,name1] + 1) 
fpkmss2 = np.log2(df.loc[:,name2] + 1)

m, b = np.polyfit(fpkmss1, fpkmss2, 1) 
x = [fpkmss1.min(), fpkmss2.max()] 

fig, ax = plt.subplots()
ax.scatter (fpkmss1, fpkmss2, s=3, alpha=0.2, color="red") 
ax.plot(x, [(m*x1+b) for x1 in x], 
    color="blue") 
ax.set_title("Scatterplot of FPKMs")
ax.set_xlabel("Log2 FPKM {}".format(name1))
ax.set_ylabel("Log2 FPKM {}".format(name2))


fig.savefig("ndscatterplot.png")



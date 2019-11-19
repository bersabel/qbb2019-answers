#!/usr/bin/env python3
import matplotlib.pyplot as plt 
import sys 

# plot postion of motif on the x-axis and freq on the y-axis

postion = []
for column in open(sys.argv[1]):
    fileds = column.strip().split('\t')
    if column[0] == "#":
        continue 
    else:
        postion.append(int(fileds[3]))
    

fig,ax = plt.subplots()
ax.hist(postion,bins=100)


ax.set_xlabel("postion")
ax.set_ylabel("freq")
fig.savefig("motif")
#!/usr/bin/env python3

"""
Usage :./01-hist
"""



import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats



#exons = []
#lengths = []
fpkms = []
for i, line in enumerate( open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]) )

my_data = np.log2( fpkms )
mu = 0
sigma = 1

x = np.linspace( -15, 15, 100 )
y = stats.norm.pdf( x, mu, sigma )

a = float(sys.argv[2])
skew_mu = float(sys.argv[3])
skew_sigma = float(sys.argv[4])
# a = -2
# mu_2 = 6
# sigma_2 = 4
# x = np.linspace( -15, 15, 100 )
y2 = stats.skewnorm.pdf( x, a, skew_mu, skew_sigma )
# ax.plot(x, stats.skewnorm.pdf(x, a),
#        'r-', lw=5, alpha=0.6, label='skewnorm pdf')


fig, ax = plt.subplots(1, 1) 
fig, ax = plt.subplots()
ax.set_title("FPKMS His")
ax.set_xlabel("FPKMS")
ax.set_ylabel("Freq")
ax.hist( my_data, bins = 100 , density = True )
ax.plot( x,y, color ="red") 
ax.plot(x,y2, label='skewnorm pdf')
ax.text(0.5, 0.95," a= 0.5, skew_mu = 4 skew_sigma=2 ", transform= ax.transAxes, fontsize=12,
        verticalalignment='top')
fig.savefig( "fpkms.png" )
plt.close( fig )
#!/usr/bin/env python3
"""

create time course
"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import os 

for i, line in enumerate( open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split()
    chromosome = fields [1]
    t_name = fields[5]
   
    if fields[2] == "+":
        new_promoter_start = int(fields[4]) - 500
        new_promoter_end = int(fields[4]) + 500
    if fields[2] == "-":
        new_promoter_start = int(fields[3]) - 500
        new_promoter_end =  int(fields[3]) + 500

    print(chromosome, new_promoter_start, new_promoter_end, t_name, sep="\t")
    
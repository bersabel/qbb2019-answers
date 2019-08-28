#!/usr/bin/env python3
import sys

for line in open( sys.argv[1]):
    
    if "DROME" in line and "FBgn" in line:
        columns = line.rstrip("\n").split()
        print(columns[-1], "\t", columns[-2] ) 
       
    else:
        continue
        


    
#!/usr/bin/env python3
import sys
Dict = {}

#create dic with two columns from q1
#sys.argv0 script
#sys.argv1 part-one file
#sys.argv2 ctab-file 
##sys.argv3 "nothing" or "default"ls
    
for line in open(sys.argv[1]):
    fields = line.rstrip("\n").split()
    flybaseID = fields[0]
    UPID = fields[1]
    Dict[flybaseID] = UPID 
    
for i, line in enumerate (open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    flybaseID_tab = fields[8]
    if flybaseID_tab in Dict:
        UPID = Dict[flybaseID_tab] 
        print(UPID,line.strip("\n"))
    elif flybaseID_tab not in Dict and sys.argv[3] == "nothing":
        continue
    elif flybaseID_tab not in Dict and sys.argv[3] == "default":  
        print("N/A",line.strip("\n")) 
    
        
# compare the flybaseid to the ctap file and if same give it the upid if not the bottom two 
   
   
    
       
    
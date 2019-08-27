#!/usr/bin/env python3
import sys

in_file = open(sys.argv[1])
count = 0
for line in in_file:
    if "NM:i:0" in line :
        count += 1
print(count)
    
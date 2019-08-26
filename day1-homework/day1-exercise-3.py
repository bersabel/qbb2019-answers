#!/usr/bin/env python3
import sys
in_file = open(sys.argv[1])
count = 0
for line in in_file:
    fields = line.strip().split("\t")
    if "NH:i:1" in fields[11:]:
        count += 1
print(count)
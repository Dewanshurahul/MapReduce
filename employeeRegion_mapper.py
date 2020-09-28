#!/usr/bin/python3

import sys
import csv

for line in csv.reader(sys.stdin):
    value = 1
    if line[34]!='Region':
        print('{0}\t{1}'.format(line[34], value))

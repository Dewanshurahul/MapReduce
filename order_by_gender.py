#!/usr/bin/python3

import sys
import csv

for line in csv.reader(sys.stdin):
    if line[5] != 'Gender':
        print('{0}\t{1}'.format(line[5], line))

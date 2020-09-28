#!/usr/bin/python3

import sys
import csv

for line in csv.reader(sys.stdin):
    value = 1
    if line[30] != 'Country':
        print('{0}\t{1}'.format(line[30], value))

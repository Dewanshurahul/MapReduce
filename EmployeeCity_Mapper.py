#!/usr/bin/python3

import sys
import csv

for line in csv.reader(sys.stdin):
    value = 1
    if line[31] != 'City':
        print('{0}\t{1}'.format(line[31], value))

#!/usr/bin/python3

import sys
import csv

for line in csv.reader(sys.stdin):
    if line[26] != 'Last % Hike':
        val = 1
        if line[26] != '0%':
            print('{0}\t{1}'.format(line[26], val))

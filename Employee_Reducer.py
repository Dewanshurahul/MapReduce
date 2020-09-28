#!/usr/bin/python3

import sys

last_key = None
current = 0
key = None

for line in sys.stdin:
    key, value = line.split('\t')
    try:
        value = int(value)
    except ValueError:
        continue
    if last_key == key:
        current += value
    else:
        if last_key:
            print('%s\t%d' % (last_key, current))
        current = value
        last_key = key

if last_key == key:
    print('%s\t%d' % (last_key, current))


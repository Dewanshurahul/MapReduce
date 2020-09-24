import sys

last_key = None
current = 0
key = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
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


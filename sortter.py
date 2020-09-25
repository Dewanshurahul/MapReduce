import sys
import operator

dic = {}
for line in sys.stdin:
	key, value = line.split('\t')
	dic[key] = value

for element in sorted(dic.keys()):
	print('{0}\t{1}'.format(str(element), dic.get(element)))

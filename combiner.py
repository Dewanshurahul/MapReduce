import sys

dic = {}
for line in sys.stdin:
	key, val = line.split('\t')
	if key in dic:
		val = dic[key]
            	dic[key] = val + 1
	else:
		dic[key] = 1

for element in dic:
	print('{0}\t{1}'.format(str(element),dic.get(element)))


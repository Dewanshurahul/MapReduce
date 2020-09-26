import sys

dic = {}
for line in sys.stdin:
	key, value = line.split('\t')
	if key in dic:
		dic.get(key).append(value)
	else:
		dic[key] = [value]

for element in dic:
	print(element, dic.get(element))

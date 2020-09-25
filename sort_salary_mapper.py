import sys
import csv

for line in csv.reader(sys.stdin):
	salary = line[25]
	if salary != 'Salary':
		print('{0}\t{1}'.format(salary, line))

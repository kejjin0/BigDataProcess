#!/usr/bin/python3

import sys
import csv

inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

count={}

with open(inputFile, "rt") as f:
	data=f.read()
	
	lines = data.split("\n")
	for row in lines:
		info = row.split("::")
		genre = info[2].split("|")
		for g in genre:
			if count.get(g) == None:
				count[g] = 1
			else:
				count[g] = count[g] + 1

with open(outputFile, "wt") as openf:
	wr = csv.writer(openf)
	wr.writerow(count.items())
	#wr.writerow(count)

	movieKey = count.keys()

	for key in movieKey:
		print("%s %s" %(key, count[key]), end='\n')
		#wr.writerow(key + ' ' + str(count[key]))

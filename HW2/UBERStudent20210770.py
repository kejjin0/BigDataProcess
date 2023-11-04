#!/usr/bin/python3

import sys
import calendar

inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])

week = ["MON", "TUE", "WED", "THU", "FTI", "SAT", "SUN"]

list = []
region = {}

with open(inputFile, "rt") as f:
	data = f.read()

	lines = data.split("\n")
	for line in lines:
		info = line.split(",")
		date = info[1].split("/")
		month = int(date[0])
		day = int(date[1])
		year = int(date[2])
		
		w = calendar.weekday(year, month, day)
		info[1] = w
		
		if region.get(info[0]) == None:
			buff = [ [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
			region[info[0]] = buff
			
		value = region[info[0]]

		##delete
		#if info[0]=='B02512':
		#	print(value)
		

		value[w][0] = str( int(value[w][0]) + int(info[2]) )
		value[w][1] = str( int(value[w][1]) + int(info[3]) )

		#if info[0]=='B02512':
		#	print(value)
		#	print('------------')
		
		region[info[0]] = value

result=[]

keys = region.keys()
for key in keys:
	for i in range(7):
		buff = [key]
		buff.append(week[i])
		value = region[key]
		buff.append(value[i][0])
		buff.append(value[i][1])
		result.append(buff)

#print(result)

with open(outputFile, "wt") as writeF:

	regionN = result[0]
	day = result[1]
	vehicles = result[2]
	trips = result[3]

	for arr in result:
		regionN = arr[0]
		day = arr[1]
		vehicles = arr[2]
		trips = arr[3]
		string = regionN + "," + day + " " + vehicles + "," + trips + "\n"
		writeF.write(string)
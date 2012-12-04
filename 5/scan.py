#!/usr/bin/env python
import pickle, urllib

with open('banner.p', 'rb') as file:
	file = pickle.loads(file)
	for line in file:
		for each_item in line:
			print (each_item[0]*each_item[1]),
		print '\n',

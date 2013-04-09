#!/usr/bin/env python
import sys
import time
def trans(string, inc):
	newstr = ''
	for i in range(len(string)):
		newstr += chr(ord(string[i])+inc)
	return newstr
cmap = {}
cfile = open('c', 'r')
for line in cfile:
	for c in line:
		if c in cmap:
			cmap[c] = cmap[c] + 1
		else:
			cmap[c] = 1
minc = -1
for c in cmap:
	if cmap[c]<minc:
		minc = cmap[c]
print c,':', minc
print cmap
cfile.close()



"""
if __name__=='__main__':
	#if len(sys.argv)!=2:
	#	print 'usage ./2.py low'
	#	sys.exit()
	#inc = int(sys.argv[1])a
	for inc in range(0, 201):
		print inc,' ',trans(cfile.readline(), inc)
		time.sleep(0.5)
"""

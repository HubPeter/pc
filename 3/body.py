#!/usr/bin/env python
import re
#read file
#match
infile = open('data', 'rb')
content = infile.read()
#content = 'iiAAAaZZZii'
mObj = re.findall(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', content, re.S)
try:
	url = ''
	for ma in mObj:
		url += ma[4]
	print url
#	print mObj.groups()
#	print mObj.group(1)
#	print mObj.group(2)
#	print mObj.group(3)
except:
	print 'No match'


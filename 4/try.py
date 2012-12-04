#!/usr/bin/env python
import urllib
import re
import time
f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579')
page = f.read()
res = []
while True:
#	time.sleep(3)
	try:
		res = re.findall('([0-9]{1,20})', page, re.S)
		#if page.find('404'):
		#	print '404'
		print res[0]
		f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+res[0])
		page = f.read()

	except:
		print page
		print res
		break
#print page


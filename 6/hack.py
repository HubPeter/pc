#!/usr/bin/env python

import zipfile, re
start = '90052'
zipname = 'channel.zip'
def main(start, zipname):
	nextnum = start
	text = ''
	zf =zipfile.ZipFile( zipname ,'r')
	comments = []
	findnothing = re.compile(r'Next nothing is (\d+)', ).match
	while True:
		try:
			text = zf.read(nextnum+'.txt')
			comments.append( zf.getinfo(nextnum+'.txt').comment )
			nextnum = findnothing(text)
			nextnum = nextnum.group(1)
		except Exception as ex:
			print 'Last ok is :', nextnum
			print text
			print ex
			break
	#collect comments
	print ''.join( comments )
if __name__=='__main__':
	main(start, zipname)	

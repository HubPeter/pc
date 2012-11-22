prestr = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
url = 'http://www.pythonchallenge.com/pc/def/map.html'
def trans(string):
	newstr = ''
	for i in range(len(string)):
		if 'a'<=string[i]<='z':
			newstr += chr(((ord(string[i])+2)-97) % 26 +97)
		else:
			newstr += string[i]
	return newstr
print trans(url)

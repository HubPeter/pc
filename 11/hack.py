#!/usr/bin/python
import Image
img = Image.open('cave.jpg')
w,h = img.size[0], img.size[1]
print img.format, img.size, img.mode
new = Image.new( img.mode, ( w , h ) );
for i in range(w*h):
	y, x = divmod( i, w )
	p = img.getpixel( (x, y) )
	if i%2:
		new.putpixel( (x/2, y/2), p )
	else:
		new.putpixel( (x/2, h/2+y/2), p )
new.save('new.jpg')
			


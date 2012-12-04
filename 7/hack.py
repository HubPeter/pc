import Image
y_begin = 0
image = Image.open('oxygen.png')
while True:
	p = image.getpixel((0, y_begin))
	if p[0] == p[1] == p[2]:
		break
	y_begin += 1
x_end = 0
while True:
	p= image.getpixel((x_end, y_begin))
	if not p[0]==p[1]==p[2]:
		break
	x_end +=1
x_cur = 0
message = []
for i in range(0, x_end, 7):
	p = image.getpixel((i, y_begin))
	message.append(chr(p[0]))
print ''.join(message)

message = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(x) for x in message])

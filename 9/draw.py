
import Image,ImageDraw
im = Image.new('RGB', (500,500))
draw = ImageDraw.Draw(im)

first=[146,399,163,403, ...]  # chunked
second=[156,141,165,135, ...] # chunked

for i in range(0, len(first), 2):
    draw.line(first[i:i + 4], fill='white')
for i in range(0, len(second), 2):
    draw.line(second[i:i + 4], fill='white')
im.save('09.jpg')

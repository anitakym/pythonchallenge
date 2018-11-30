from PIL import Image

im = Image.open('cave.jpg')
print(im.mode)
print(im.size)
odd = Image.new(im.mode, (im.size[0]//2, im.size[1]//2))
even = Image.new(im.mode, (im.size[0]//2, im.size[1]//2))

for x in range(1, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        odd.putpixel(((x-1)//2, (y-1)//2), im.getpixel((x, y)))

for x in range(1, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        odd.putpixel((x//2, y//2), im.getpixel((x, y)))

odd.show()
even.show()

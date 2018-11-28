# S  DOTALL      "." matches any character at all, including the newline.
# “.” Matches any character except a newline.
import re
from PIL import Image

file = open('task10.html')
# print(file.read())
message = re.findall('(<!--[^-]+-->)', file.read(), re.S)[1]
file.close()
firstp = re.findall('first:(.+)second', message, re.S)[0]
first = re.findall('(\d+)', firstp, re.S)
secondp = re.findall('second:(.+)', message, re.S)[0]
second = re.findall('(\d+)', secondp, re.S)

all = first + second

im = Image.open('good.jpg')
im2 = Image.new(im.mode, im.size)

for x in range(0, len(all), 2):
    im2.putpixel((int(all[x]), int(all[x+1])), (255, 255, 255, 255))

im2.show()
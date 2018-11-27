# pip3 install python3-pil
# QQ 截图得到像素坐标 （0， 607） （42， 51）

from PIL import Image
img = Image.open('oxygen.png')
# print(img.size)
# data = [img.getpixel((i, j)) for i in range(0, 609) for j in range(43, 53)]
row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
print("".join(row))
print(''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))
# print(data)

f = open('evil2.gfx', 'rb')
content = f.read()
f.close()
print(len(content))
for i in range(5):
    f = open('./task13/%d.png' % i, 'wb')
    f.write(content[i::5])
    f.close()
print('ok')
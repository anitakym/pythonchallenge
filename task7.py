# hockey->oxygen
import re
import zipfile

findnothing = re.compile(r'Next nothing is (\d+)').match
comments = []
z = zipfile.ZipFile('channel.zip', 'r')
seed = '90052'

while True:
    fname = seed + '.txt'
    # text = open('channel/' + fname, 'r').read()
    comments.append((z.getinfo(fname).comment).decode())
    guts = (z.read(fname).decode())
    # m = findnothing(text)
    m = findnothing(guts)
    if m:
        seed = m.group(1)
    else:
        break

print(''.join(comments))

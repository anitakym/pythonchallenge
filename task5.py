import re
from urllib import request
from urllib import parse
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

search = re.compile("(\d*)$")
search_html = re.compile("\.html$")

for i in range(400):
    print("%s: " % nothing, end='')

    line = request.urlopen("%s%s" % (url, nothing)).read().decode('utf-8')
    print(line)

    if search_html.findall(line):
        break
    match = search.findall(line)
    if match:
        nothing = match[0]
    else:
        nothing = str(int(nothing)/2)

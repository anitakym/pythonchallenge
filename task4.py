'''One small letter, surrounded by three big bodyguards on each of its sides.'''

'''xXXXxXXXx'''

import re
text = open('origin4.txt').read()
print(''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text)))

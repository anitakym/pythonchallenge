# find rare characters in the mess below
import string
ORIGIN = open('origin.txt').read()
# print(ORIGIN)

def find_rare(origin_str):
    res = list(filter(lambda x: x in string.ascii_letters, origin_str))
    print(res)

find_rare(ORIGIN)

'''
standard:
s = ''.join([line.rstrip() for line in open('mess.txt')])    
occ = {}

for c in s: 
    occ[c] = occ.get(c, 0) + 1  # 相同的字符，字典的值加1
    avgOC = len(s) // len(occ)

print(''.join([c for c in s if occ[c] < avgOC]))
# 引用字典的值的时候最好用occ.get(c)而不是 occ[c]，否则很容易出现KeyError
'''

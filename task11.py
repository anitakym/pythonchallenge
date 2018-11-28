# a = [1, 11, 21, 1211, 111221, 
# a[30]
# %c 字符及其ASCII码 %s 字符串 %d 有符号整数(十进制)
# 计数器
strings = ['1', '11']

for i in range(1, 31):
    j = 0
    temp = ''
    while j < len(strings[i]):
        count = 1
        while j < (len(strings[i]) - 1) and (strings[i][j] == strings[i][j+1]):
            j = j + 1
            count = count + 1
        temp = '%s%d%c' % (temp, count, strings[i][j])
        j = j + 1
    strings.append(temp)

print(len(strings[30]))

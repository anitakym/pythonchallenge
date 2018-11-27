#用python3的话，会报错AttributeError: 'bytes' object has no attribute 'encode',去掉encode
import pickle

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size)
    def readline(self, size=-1):
        return self.fileobj.readline(size)

data = pickle.load(StrToBytes(open('banner.p', 'rb')))

'''for each in data:
    print(each)'''
for each in data:
    print("".join([i[1] * i[0] for i in each]))

'''for each in data:
    for i in each:
        print("".join([i[1] * i[0]]))'''
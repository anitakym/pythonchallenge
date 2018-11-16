'''js:String.fromCharCode(), string.charCodeAt()'''
'''help(str.maketrans)'''
import string

# STR = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
STR = 'map'
'''getstr'''
def change_str(str_letter):
    if str_letter is 'y':
        return 'a'
    if str_letter is 'z':
        return 'b'
    if str_letter.isalpha():
        return chr(ord(str_letter) + 2)
    return str_letter

def std_change(text):
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    print(text.translate(table))

RES = map(change_str, STR)
std_change(STR)
print(''.join(RES))

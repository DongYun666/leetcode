# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 20:04
# @Author : DongYun
# @File : HJ29 字符串加解密.py
# @Software : PyCharm

def Encoder(ch):
    res = ""
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                res += chr((ord(ch) - ord("a") + 1) % 26 + ord("a")).upper()
            else:
                res += chr((ord(ch) - ord("A") + 1) % 26 + ord("A")).lower()
        else:
            res+=chr((ord(ch)-ord("0")+1)%10+ord("0"))
    return res
def Decoder(ch):
    res = ""
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                res += chr((ord(ch) - ord("a") - 1) % 26 + ord("a")).upper()
            else:
                res += chr((ord(ch) - ord("A") - 1) % 26 + ord("A")).lower()
        else:
            res+=chr((ord(ch)-ord("0")-1)%10+ord("0"))
    return res
while True:
    try:
        s = input()
        print(Encoder(s))
        s = input()
        print(Decoder(s))
    except:
        break


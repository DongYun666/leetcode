# -*- codeing = utf-8 -*-
# @Time : 2022/4/21 21:02
# @Author : DongYun
# @File : HJ82 将真分数分解为埃及分数.py
# @Software : PyCharm

def to_Egypt_score(molecule, denominator):
    res = []
    if molecule == 1 or denominator%molecule == 0:
        print("1"+"/"+str(int(denominator/molecule)))
    mo = 1
    de = 2
    temp = 2
    while mo*denominator != de*molecule:
        if temp == 2:
            if de*molecule > mo*denominator:
                res.append(temp)
            temp+=1
        else:
            if ((de+1)*temp) * molecule < (mo*temp+1) * denominator:
                temp+=1
            else:
                res.append(temp)
                mo = mo*temp+1
                de = (de+1)*temp
    print(res)


while True:
    try:
        s = input().split("/")
        print(to_Egypt_score(int(s[0]),int(s[1])))
    except:
        break

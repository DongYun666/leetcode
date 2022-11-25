# -*- codeing = utf-8 -*-
# @Time : 2022/4/19 20:18
# @Author : DongYun
# @File : 容易级别.py
# @Software : PyCharm

while True:
    try:
        s = input()
        count = [0]*4
        res = 0
        for ch in s:
            if ch == "E" or ch == "e":
                count[0]+=1
            if ch == "A" or ch == "a":
                count[1]+=1
            if ch == "S" or ch == "s":
                count[2]+=1
            if ch == "Y" or ch == "y":
                count[3]+=1
                if count.count(0) == 0:
                    res+=1
                    count = [0]*4
        print(res)
    except:
        break

# abcdesAssayEaaaassYyy
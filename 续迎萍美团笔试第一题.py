# -*- codeing = utf-8 -*-
# @Time : 2022/4/30 9:53
# @Author : DongYun
# @File : 续迎萍美团笔试第一题.py
# @Software : PyCharm


while True:
    try:
        s = input()
        t = input()
        temp = {}
        for index in range(len(t)-len(s)):
            if t[index:index+len(s)] not in temp.keys():
                temp[t[index:index+len(s)]] = 0
            else:
                temp[t[index:index+len(s)]]+=1
        record = []
        for key,value in temp.items():
            count = 0
            for i in range(len(s)):
                if key[i] != s[i]:
                    count+=1
            record.append(count)
        res = 0
        j=0
        for x in temp.values():
            res+=x*record[j]
            j+=1
        print(j)
    except:
        break
# -*- codeing = utf-8 -*-
# @Time : 2022/4/18 19:31
# @Author : DongYun
# @File : HJ63 DNA序列.py
# @Software : PyCharm

while True:
    try:
        DNA = input()
        lenght = int(input())
        GC_Ratio = 0
        res = ""
        if lenght>=len(DNA):
            print(DNA)
        for index in range(0,len(DNA)-lenght):
            temp = DNA[index:index+lenght]
            now_GC_Ratio = (temp.count('C') + temp.count('G')) / lenght
            if GC_Ratio < now_GC_Ratio:
                GC_Ratio = now_GC_Ratio
                res = temp
        print(res)
    except:
        break
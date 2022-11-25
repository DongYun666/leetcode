# -*- codeing = utf-8 -*-
# @Time : 2022/4/29 19:59
# @Author : DongYun
# @File : 美团2021校招笔试3.py
# @Software : PyCharm

while True:
    try:
        T = int(input()) #数据组数
        for _ in range(T):
            N = int(input()) #餐桌数
            can_use_count = list(input()) #每张餐桌用餐人数
            M = int(input()) # 排队人数
            paidui_sex = input() #排队人性别
            for se in paidui_sex:
                if se == "M":
                    if "1" in can_use_count:
                        index = can_use_count.index("1")
                        print(index+1)
                        can_use_count[index] = "2"
                    else:
                        index = can_use_count.index("0")
                        print(index + 1)
                        can_use_count[index] = "1"
                else:
                    if "0" in can_use_count:
                        index = can_use_count.index("0")
                        print(index+1)
                        can_use_count[index] = "1"
                    else:
                        index = can_use_count.index("1")
                        print(index + 1)
                        can_use_count[index] = "2"
    except:
        break

# -*- codeing = utf-8 -*-
# @Time : 2022/4/14 21:17
# @Author : DongYun
# @File : HJ50.py
# @Software : PyCharm
# s = input().replace("{","(").replace("}",")").replace("[","(").replace("]",")")
# print(int(eval(input().replace("{","(").replace("}",")").replace("[","(").replace("]",")")
# )))

s = input()
stack_num = []
stack_opr = []
for ch in s:
    if ch.isdigit():
        stack_num.append(int(ch))
    elif :
        stack_opr.append(ch)
    if ch!= ')' and ch != "]" and ch != "}":
        stack.append(ch)
    print(stack)

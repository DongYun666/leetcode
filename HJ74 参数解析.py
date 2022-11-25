# -*- codeing = utf-8 -*-
# @Time : 2022/4/19 19:11
# @Author : DongYun
# @File : HJ74 参数解析.py
# @Software : PyCharm
while True:
    try:
        str1 = input().replace(' ','\n')
        # print(str1)
        e = ""
        flag = False
        for i in str1:
            if i == '"':
                flag = not flag
            elif flag == True and i == '\n':
                e += ' '
            else:
                e+=i
        b = e.count('\n')+1
        print(b)
        print(e)
    except:
        break


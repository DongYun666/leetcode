# -*- codeing = utf-8 -*-
# @Time : 2022/4/13 22:52
# @Author : DongYun
# @File : HJ33 整数与IP地址间的转换.py
# @Software : PyCharm
while True:
    try:
        IP = input().split(".")
        num = int(input())
        res = ""
        for x in IP:
            res += "0"*(8-len(bin(int(x)))+2)+bin(int(x))[2:]
        print(int(res,2))
        num_IP = bin(num)[2:]
        if len(num_IP)%8!=0:
            num_IP = "0"*(8-len(num_IP)%8)+num_IP
        num_IP_res = ""
        for i in range(0,len(num_IP),8):
            num_IP_res+=str(int(num_IP[i:i+8],2))
            if i != len(num_IP)-8:
                num_IP_res+="."
        print(num_IP_res)
    except:
        break
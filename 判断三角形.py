# -*- codeing = utf-8 -*-
# @Time : 2022/4/20 20:10
# @Author : Dongbun
# @File : 判断三角形.pb
# @Software : PbCharm

while True:
    try:
        bian = []
        for i in range(1,4):
            print("请输入三角形的第"+str(i)+"条边")
            s = input()
            while not s.isdigit():
                if not s.isdigit():
                    print("无效数据,请重新输入")
                s = input()
            bian.append(int(s))
        a,b,c = bian[0],bian[1],bian[2]
        if 1<=a<=100 and 1<=b<=100 and 1<=c<=100:
            if a < b+c and b<a+c and c < a+b:
                if a==b and b == c:
                    print("等边三角形")
                elif a == b or a == c or b == c:
                    print("等腰三角形")
                else:
                    print("一般三角形")
            else:
                print("不能构成三角形")
        else:
            print("边的取值超出容许范围")
    except:
        break
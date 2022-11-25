# -*- codeing = utf-8 -*-
# @Time : 2022/4/18 19:48
# @Author : DongYun
# @File : HJ64 MP3光标位置.py
# @Software : PyCharm

while True:
    try:
        count = int(input())
        order = input()
        now = 1
        # window = [x for x in range(1,count+1)]
        window_top = 1
        for s in order:
            if s == "U":
                if now == 1 and count>4:
                    now = count
                    window_top = count-3
                    # print(window_top)
                else:
                    if now == window_top and count>4:
                        window_top-=1
                    now = (now+count-1)%count
                    # print(window_top)
            if s == "D":
                if now == count and count>4:
                    window_top = 1
                if window_top == now-3:
                    window_top+=1
                if now == count-1:
                    now = count
                else:
                    now = (now+1+count)%count
            # print(now)
            print(window_top)
        if count>4:
            for i in range(3):
                print(window_top+i,end=" ")
            print(window_top+3)
        else:
            for i in range(count-1):
                print(window_top+i,end= " ")
            print(window_top+count-1)
        print(now)
    except:
        break

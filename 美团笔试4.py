# -*- codeing = utf-8 -*-
# @Time : 2022/4/25 19:27
# @Author : DongYun
# @File : 美团笔试4.py
# @Software : PyCharm


# all([a[i] < a[i+1] for i in range(len(a)-1)])

while True:
    try:
        max_num,num_len = list(map(int,input().split()))
        seriel = list(map(int,input().split()))
        count = 0
        def check(l,r):
            pre = 0
            for x in seriel:
                if x<l or x>r:
                    if pre <= x:
                        pre = x
                    else:
                        return False
            return True
        for i in range(1,max_num+1):
            left,right = i,max_num+1
            while left<right:
                mid = (left+right)//2
                if check(i,mid):
                    right = mid
                else:
                    left = mid +1
            if left == max_num+1:
                break
            count+=max_num+1-left


        print(count)
    except:
        break



        # for l in range(1,max_num+1):
        #     for r in range(l,max_num+1):
        #         temp = [0]
        #         index = 0
        #         for index,x in enumerate(seriel):
        #             if 0<x<l or r<x<max_num+1:
        #                 if x >= temp[len(temp)-1]:
        #                     temp.append(x)
        #                 else:
        #                     break
        #             if index == len(seriel)-1:
        #                 count+=1





# -*- codeing = utf-8 -*-
# @Time : 2021/12/18 11:06
# @Author : DongYun
# @File : My_math.py
# @Software : PyCharm
import math


def get_mean(list_x):
    sum = 0
    for x in list_x:
        sum+=x
    return sum/len(list_x)

def get_std(list_x):
    resoult = 0
    mean = get_mean(list_x)
    for x in list_x:
        resoult += (x-mean)**2
    return resoult/(len(list_x)-1)

# list_x = [0,1,3,2,1,2,-1,2]
# print(get_mean(list_x))
# print(math.sqrt(get_std(list_x)))

def get_D_cha(list_x,list_y):
    y_index = 0
    new_list = []
    for x in list_x:
        print(x)
        print(list_y[y_index])
        new_list.append(float(x-list_y[y_index]))
        y_index+=1
    return new_list
print(get_D_cha([6.6,7.0,8.3,8.2,5.2,9.3,7.9,8.5,7.8,7.5,6.1,8.9,6.1,9.4,9.1],
                [7.4,5.4,8.8,8.0,6.8,9.1,6.3,7.5,7.0,6.5,4.4,7.7,4.2,9.4,9.1]))
list_x = [-0.8,1.6,-0.5,0.2,-1.6,0.2,1.6,1.0,0.8,1.0,1.7,1.2,1.9,0.0,0.0]
print(get_mean(list_x))
print(math.sqrt(get_std(list_x)))
# -*- codeing = utf-8 -*-
# @Time : 2022/3/14 20:47
# @Author : DongYun
# @File : test2.py
# @Software : PyCharm
# from decimal import Decimal

# x = 20
# res = -1.0

# while x != 0:
#     res+=0.1
#     print("%.1f"%res)
#     x-=1

# from collections import defaultdict


# barcodes = [1,2,1]
# c_dict = defaultdict(int)
# # 列表中的元素出现的次数
# for i in barcodes:
#     c_dict[i] += 1
# print(c_dict)
# # 按照出现次数排序

# print(sorted(c_dict.items(), key=lambda x: x[1], reverse=True))
# #barcodes.sort(key=lambda x: barcodes.count(x))
# nums = [1,2,3,4,5,6,7,8,9]
# for num in reversed(nums):
#     print(num)
# print(nums.reverse())
# print(nums)
word = "abcdefd"
ch = "z"
# print(word.index(ch))
try:
    print(word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:])
except:
    print(word)
# print(word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:])
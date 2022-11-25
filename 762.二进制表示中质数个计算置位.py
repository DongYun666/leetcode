# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 9:48
# @Author : DongYun
# @File : 762.二进制表示中质数个计算置位.py
# @Software : PyCharm
from math import sqrt

#
# class Solution:
#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         res = 0
#         def count_1_in_x(x):
#             count = 0
#             while x>0:
#                 x &=(x-1)
#                 count+=1
#             return count
#         def Prime_number(x):
#             if x <= 1:
#                 return False
#             if x == 2 or x == 3:
#                 return True
#             for i in range(2,int(sqrt(x))+1):
#                 if x % i == 0:
#                     return False
#             return True
#         for x in range(left,right+1):
#             count_1 = count_1_in_x(x)
#             if Prime_number(count_1):
#                 res+=1
#         return res

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # for m in range(left, right + 1):
        #     print(m.bin_count())
        # return 0
        return sum([(665772 >> m.bit_count()) & 1 for m in range(left, right + 1)])
left = 6
right = 10
print(Solution().countPrimeSetBits(left,right))

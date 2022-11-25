# -*- codeing = utf-8 -*-
# @Time : 2022/4/1 10:26
# @Author : DongYun
# @File : 954.二倍数对数组.py
# @Software : PyCharmclass Solution:
#     def canReorderDoubled(self, arr: List[int]) -> bool:
#         if 0 in arr:
#             return False
#         arr.sort()
#         for i in range(0,len(arr),2):
#             if arr[i] < 0 and arr[i] != 2*arr[i+1] or arr[i] > 0 and 2*arr[i] != arr[i+1] or arr[i] == 0:
#                 return False
#         return True
from collections import Counter
from typing import List


arr = [2,4,0,0,8,1]
print(Solution().canReorderDoubled(arr))


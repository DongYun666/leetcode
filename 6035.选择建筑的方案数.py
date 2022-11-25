# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 20:17
# @Author : DongYun
# @File : 6035.选择建筑的方案数.py
# @Software : PyCharm
from itertools import combinations

# class Solution:
#     def numberOfWays(self, s: str) -> int:
#          res = 0
#          for x in  combinations(s,3):
#              if x == ("1","0","1") or x == ("0","1","0"):
#                 res+=1
#          return res
class Solution:
    def numberOfWays(self, s: str) -> int:
        count_0 = s.count("0")
        n = len(s)
        ans,ch_0 = 0,0
        for index,ch in enumerate(s):
            if ch == "1":
                ans += ch_0 * (count_0-ch_0)
            else:
                ans += (index-ch_0) * (n-count_0-index+ch_0)
                ch_0+=1
        return ans
s = "001101"
print(Solution().numberOfWays(s))

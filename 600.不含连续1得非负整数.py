# -*- codeing = utf-8 -*-
# @Time : 2022/7/29 15:24
# @Author : DongYun
# @File : 600.不含连续1得非负整数.py
# @Software : PyCharm
class Solution:
    global count,g_n
    count = 1
    g_n = 0
    def dfs(self,n):
        global g_n,count
        if n > g_n:
            return
        count+=1
        # print(n)
        if n & 1:
            self.dfs(n<<1)
        else:
            self.dfs(n<<1)
            self.dfs((n<<1)+1)
        return
    def findIntegers(self, n: int) -> int:
        global g_n,count
        g_n = n
        self.dfs(1)
        return count





print(Solution().findIntegers(2))
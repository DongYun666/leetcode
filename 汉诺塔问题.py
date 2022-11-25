# -*- codeing = utf-8 -*-
# @Time : 2021/11/25 19:00
# @Author : DongYun
# @File : 汉诺塔问题.py
# @Software : PyCharm
class Solution:
    def hanoi(self,n,a,b,c):
        def dfs(n,a,b,c):
            if n == 1:
                print(a+"->"+c)
                return
            else:
                dfs(n-1,a,c,b)
                print(a+"->"+c)
                dfs(n-1,b,a,c)
        dfs(n,a,b,c)

print(Solution().hanoi(3,'A','B','C'))

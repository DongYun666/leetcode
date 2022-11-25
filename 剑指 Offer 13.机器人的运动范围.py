# -*- codeing = utf-8 -*-
# @Time : 2022/3/21 9:47
# @Author : DongYun
# @File : 剑指 Offer 13.机器人的运动范围.py
# @Software : PyCharm

class Solution:
    ##逐行统计
    def movingCount2(self, m: int, n: int, k: int) -> int:
        count = 1
        visit = [(0, 0)]
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in visit or (i, j - 1) in visit) and i // 10 + i % 10 + j // 10 + j % 10 <= k:
                    visit.append((i, j))
                    count += 1
        return count

    ##dfs
    def movingCount(self, m: int, n: int, k: int) -> int:
        visit = []
        def dfs(x,y):
            if (x,y) not in visit and 0 <=x <m and 0<=y <n and x//10+x%10+y//10+y%10 <= k:
                visit.append((x,y))
                return 1+dfs(x+1,y)+dfs(x,y+1)
            else:
                return 0
        return dfs(0,0)

    ##BFS
    def movingCount3(self, m: int, n: int, k: int) -> int:
        visit = [(0,0)]
        query = [(0,0)]  ##创建队列
        while query:
            temp = query.pop()
            x,y = temp[0],temp[1]
            if (x+1)<m and y<n and (x+1,y) not in visit and (x+1) // 10 + (x+1) % 10 + y // 10 + y % 10 <= k:
                query.append((x+1,y))
                visit.append((x+1,y))
            if x<m and (y+1)<n and (x,y+1) not in visit and x // 10 + x % 10 + (y+1) // 10 + (y+1) % 10 <= k:
                query.append((x,y+1))
                visit.append((x,y+1))
        return len(visit)



m =1
n =2
k =1
print(Solution().movingCount3(m,n,k))
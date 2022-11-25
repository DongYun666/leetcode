from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        avg = sum(cookies)//k
        flag = [False]*len(cookies)

        def dfs(avg,temp,k):
            if k == 0:
                #全部分配完成
            if temp >= avg:
                dfs(avg,0,k-1)
            for i in range(len(cookies)):
                if flag[i] == True:
                    continue
                flag[i] = True
                if temp<avg and dfs()
                flag[i] = False




cookies = [8, 15, 10, 20, 8]
k = 2
print(Solution().distributeCookies(cookies, k))
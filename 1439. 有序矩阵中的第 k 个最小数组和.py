from typing import List
class Solution:
    # 暴力法
    # def kthSmallest(self, mat: List[List[int]], k: int) -> int:
    #     row = mat[0]
    #     for i in range(1,len(mat)):
    #         row = sorted([x+y for x in row for y in mat[i]])[:k]
    #     return row[-1]

    # 二分法 + dfs
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m,n = len(mat),len(mat[0])
        left,right = sum([mat[i][0] for i in range(m)]),sum([mat[i][-1] for i in range(m)])
        init = left
        while left < right:
            mid = (left + right) // 2
            def dfs(i,cur):
                if i == m:
                    return 1
                res = 0
                for j in range(n):
                    if cur + mat[i][j] - mat[i][0] <= mid:
                        res += dfs(i+1,cur+mat[i][j]-mat[i][0])
                        if res > k:
                            return res
                    else:
                        break
                return res
            cnt = dfs(0,init)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return right


mat = [[1,3,11],[2,4,6]]
k = 5

mat = [[1,3,11],[2,4,6]]
k = 9
print(Solution().kthSmallest(mat,k))
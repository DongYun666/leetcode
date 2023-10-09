from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left,right,res = 1,position[-1]-position[0],-1
        def check(mid):
            cnt = 1
            cur = position[0]
            for i in range(1,len(position)):
                if position[i] - cur >= mid:
                    cnt += 1
                    cur = position[i]
            return cnt >= m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
position = [1,2,3,4,7]
m = 3
position = [5,4,3,2,1,1000000000]
m = 2
print(Solution().maxDistance(position,m))
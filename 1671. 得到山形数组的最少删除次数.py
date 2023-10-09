from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and pre[j]+1 > pre[i]:
                    pre[i] = pre[j] + 1
        post = [0] * n
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[j] < nums[i] and post[j] + 1 > post[i]:
                    post[i] = post[j] + 1
        res = n
        for i in range(n):
            if pre[i] and post[i] and n-pre[i]-post[i]-1 < res:
                res = n-pre[i]-post[i]-1
        return res

nums = [2, 1, 1, 5, 6, 2, 3, 1]
print(Solution().minimumMountainRemovals(nums))
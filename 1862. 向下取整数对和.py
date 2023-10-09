from typing import List
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        max_num = max(nums)
        cnt = [0] * (max_num + 1)
        for num in nums:
            cnt[num] += 1
        pre = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            pre[i] = pre[i - 1] + cnt[i]
        res = 0
        for y in range(1, max_num + 1):
            if cnt[y] == 0:
                continue
            d = 1
            while d * y <= max_num:
                res += cnt[y] * d * (pre[min((d + 1) * y - 1, max_num)] - pre[d * y - 1])
                d += 1
        return res % mod
    
nums = [2,5,9]
nums = [7,7,7,7,7,7,7]
print(Solution().sumOfFlooredPairs(nums))
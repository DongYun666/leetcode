from collections import Counter, defaultdict
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # 使用滑动窗口
        #1、统计所有出现元素
        count = len(Counter(nums))
        res = 0
        n = len(nums)
        for i in range(n):
            j = i
            temp = defaultdict(int)
            while j < n:
                temp[nums[j]] += 1
                if len(temp) == count:
                    res += n-j
                    break
                j += 1
        return res

nums = [1,3,1,2,2]
nums = [5,5,5,5]
print(Solution().countCompleteSubarrays(nums))
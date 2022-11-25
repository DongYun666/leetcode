from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        cnt = defaultdict(int)
        res = 0
        end = -1
        pre_sum = 0
        for start in range(len(nums)):
            if start != 0:
                cnt.pop(nums[start - 1])
                pre_sum -= nums[start - 1]
            while end + 1 < len(nums) and not cnt.get(nums[end + 1], None):
                cnt[nums[end + 1]] = 1
                pre_sum += nums[end + 1]
                end += 1
            res = max(res, pre_sum)
        return res



s = "abab"
p = "ab"

s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def count(s1, s2):
            ans = 0
            for i in range(len(s1)):
                for j in range(len(s2)):
                    if s1[i] > 2*s2[j]:
                        ans += 1
            return ans
        def merge_count(s):
            n = len(s)
            if n < 2:
                return
            mid = n // 2
            s1 = s[:mid]
            s2 = s[mid:]
            merge_count(s1)
            merge_count(s2)
            nonlocal res
            res += count(s1, s2)
        merge_count(nums)
        return res

nums = [1, 3, 2, 3, 1]
nums = [2,4,3,5,1]
print(Solution().reversePairs(nums))
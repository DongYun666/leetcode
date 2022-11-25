from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        ans = float("-inf")
        for g in gain:
            ans = max(ans, res[-1] + g)
            res.append(res[-1]+g)
        return ans

gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))

from typing import List
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []
        ans = 0
        i = 1
        while len(res) < n:
            if k - i in res:
                i += 1
                continue
            ans += i
            res.append(i)
            i += 1
        return ans


n = 5
k = 4           
print(Solution().minimumSum(n,k))
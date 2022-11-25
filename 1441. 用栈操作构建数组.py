from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        tar_max = max(target)
        res = []
        pre = 1
        for t in target:
            res+=["push","pop"]*(t-pre-1)
            res.append("push")
            pre = t
        return res



target = [1, 2]
n = 4
print(Solution().buildArray(target, n))

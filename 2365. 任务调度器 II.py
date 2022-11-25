from collections import defaultdict
from typing import List
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        res = 0
        last = defaultdict()
        for task in tasks:
            res += 1
            if task in last.keys():
                res = max(res, last[task]+space+1)
            last[task] = res
        return res



tasks = [1, 2, 1, 2, 3, 1]
space = 3
print(Solution().taskSchedulerII(tasks, space))
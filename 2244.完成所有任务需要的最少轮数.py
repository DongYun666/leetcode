from collections import Counter
from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_count = Counter(tasks)
        res = 0
        for task,count in tasks_count.items():
            x = count % 3
            if count == 1:
                return -1
            if x == 0:
                res+=count//3
            else:
                res += count//3+1
        return res



tasks = [2,2,3,3,2,4,4,4,4,4]
# tasks = [5,5,5,5]
tasks = [2,3,3]
print(Solution().minimumRounds(tasks))
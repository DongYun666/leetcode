from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = list(Counter(tasks).values())
        max_exec = max(freq)
        max_count = freq.count(max_exec)
        return max(len(tasks),(max_exec-1)*(n+1) + max_count)


tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2

# tasks = ["A","A","A","B","B","B"]
# n = 0
#
# tasks = ["A","A","A","B","B","B"]
# n = 2
print(Solution().leastInterval(tasks, n))
from collections import defaultdict
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = defaultdict(int)
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted(diff.keys())
        n = len(people)
        res = [0] * n
        i = sum = 0
        for p,id in sorted(zip(people,range(n))):
            while i < len(times) and times[i] <= p:
                sum += diff[times[i]]
                i += 1
            res[id] = sum
        return res
    

flowers = [[1,6],[3,7],[9,12],[4,13]]
persons = [2,3,7,11]

flowers = [[1,10],[3,3]]
persons = [3,3,2]

flowers = [[19,37],[19,38],[19,35]]
persons = [6,7,21,1,13,37,5,37,46,43]
print(Solution().fullBloomFlowers(flowers, persons))    
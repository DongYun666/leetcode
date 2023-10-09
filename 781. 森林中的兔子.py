from collections import Counter
from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for k,v in count.items():
            res += (v//(k+1))*(k+1)
            if v%(k+1):
                res += (k + 1)
        return res
    
answers = [1,1,2]
# answers = [10,10,10]
print(Solution().numRabbits(answers))
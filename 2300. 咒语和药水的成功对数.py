import bisect
from collections import defaultdict
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i in range(len(spells)):
            spells[i] = (success+spells[i]-1)//spells[i]
        res = []
        # print(potions,spells)
        for spell in spells:
            res.append((len(potions)-bisect.bisect_left(potions,spell)))
        return res

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(Solution().successfulPairs(spells,potions,success))


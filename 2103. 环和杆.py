from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        dict = defaultdict(set)
        for ring,num in zip(rings[::2],rings[1::2]):
            dict[num].add(ring)
        res  = 0
        for r in dict.values():
            if r == {"R","B","G"}:
                res += 1
        return res
rings = "B0B6G0R6R0R6G9"
print(Solution().countPoints(rings))
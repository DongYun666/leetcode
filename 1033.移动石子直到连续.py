from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        min_move,max_move = 0,0
        if a+1 != b:
            min_move += 1
            max_move += (b-a-1)
        if b+1 != c:
            min_move += 1
            max_move += (c-b-1)
        return [min_move,max_move]


a = 4
b = 3
c = 2
print(Solution().numMovesStones(a,b,c))
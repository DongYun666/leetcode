from collections import defaultdict
from typing import List
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dict = defaultdict(int)
        for row in matrix:
            if row[0] == 0:
                dict[tuple(row)] += 1
            else:
                dict[tuple([1-i for i in row])] += 1
        return max(dict.values())
matrix = [[0,1],[1,1]]
matrix = [[0,0,0],[0,0,1],[1,1,0]]
print(Solution().maxEqualRowsAfterFlips(matrix))
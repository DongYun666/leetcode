from typing import List
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        res = [[0] * len(colsum),[0] * len(colsum)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                res[0][i],res[1][i] = 1,1
                upper -= 1
                lower -= 1
            elif colsum[i] == 0:
                continue
            else:
                if upper > lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return []
        return res
upper = 2
lower = 1
colsum = [1,1,1]

upper = 2
lower = 3
colsum = [2,2,1,1]
print(Solution().reconstructMatrix(upper,lower,colsum))
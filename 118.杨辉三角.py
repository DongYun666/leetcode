from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        for _ in range(numRows-2):
            temp = res[-1]
            ans = [1]
            for i in range(len(temp)-1):
                ans.append(temp[i]+temp[i+1])
            ans.append(1)
            res.append(ans)
        return res



numRows = 5
print(Solution().generate(numRows))
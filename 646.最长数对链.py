from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        res,cur = 0,float('-inf')
        for i in range(len(pairs)):
            if cur < pairs[i][0]:
                res+=1
                cur = pairs[i][1]
        return res


num = [[1,2], [2,3], [3,4]]
print(Solution().findLongestChain(num))
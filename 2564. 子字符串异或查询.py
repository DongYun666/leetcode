from typing import List
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        res = []
        queries = [bin(x ^ y)[2:] for x,y in queries]
        for query in queries:
            index = s.find(query)
            res.append([index,index+len(query)-1])
        return res
s = "101101"
queries = [[0,5],[1,2]]
print(Solution().substringXorQueries(s,queries))
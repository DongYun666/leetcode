from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []
        for query in queries:
            for diction in dictionary:
                t = 0
                for i in range(n):
                    if query[i]!=diction[i]:
                        t+=1
                if t<=2:
                    res.append(query)
                    break
        return res

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]

# queries = ["yes"]
# dictionary = ["not"]
print(Solution().twoEditWords(queries, dictionary))
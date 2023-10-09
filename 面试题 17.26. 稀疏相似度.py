from collections import defaultdict
from  typing import List
class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        dect = defaultdict(list)
        for i in range(len(docs)):
            for j in range(len(docs[i])):
                dect[docs[i][j]].append(i)
        count = defaultdict(int)
        for key,value in dect.items():
            if len(value) > 1:
                for i in range(len(value)):
                    for j in range(i+1,len(value)):
                        count[(value[i],value[j])] += 1
        res = []
        for key,value in count.items():
            res.append(str(key[0]) + "," + str(key[1]) + ": " + "{:.4f}".format(value/(len(docs[key[0]]) + len(docs[key[1]]) - value)).zfill(6))
        return res
docs = [
  [14, 15, 100, 9, 3],
  [32, 1, 9, 3, 5],
  [15, 29, 2, 6, 8, 7],
  [7, 10]
]
print(Solution().computeSimilarities(docs))
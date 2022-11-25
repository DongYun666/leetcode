from collections import defaultdict
from typing import List
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        dict = defaultdict()
        for i,node in enumerate(edges):
            if node in dict:
                dict[node]+=i
            else:
                dict[node]=i
        dict = sorted(dict.items(),key=lambda x:(-x[1],x[0]))
        # dict.sort(key=lambda x: x[1])
        return dict[0][0]
edges = [1, 0, 0, 0, 0, 7, 7, 5]
print(Solution().edgeScore(edges))
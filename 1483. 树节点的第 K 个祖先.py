import math
from typing import List
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = int(math.log(n,2)) + 1
        self.dp = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        for j in range(1,self.log):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
        print(self.dp)
    def getKthAncestor(self, node: int, k: int) -> int:
        return self.dp[node][k-1] if k < self.log else -1
        # for i in range(self.log-1,-1,-1):
        #     if k & (1 << i):
        #         node = self.dp[node][i]
        #         if node == -1:
        #             return -1
        # return node




n = 10
parent = [-1,0,0,1,2,0,1,3,6,1]
obj = TreeAncestor(n, parent)
print(obj.getKthAncestor(7,3))
# print(obj.getKthAncestor(3,2))
# print(obj.getKthAncestor(0,1))
# print(obj.getKthAncestor(3,1))
# print(obj.getKthAncestor(3,5))

# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[10,],[8,6],[9,7],[1,1],[2,5],[4,2],[7,3],[3,7],[9,6],[3,5],[8,8]]


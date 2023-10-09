from typing import List
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        m = k.bit_length() - 1
        pa = [[(p,p)] + [None] * m for p in receiver]
        for i in range(m):
            for x in range(n):
                p,s = pa[x][i]
                pp,ss = pa[p][i]
                pa[x][i+1] = (pp,ss+s)
        res = 0
        for i in range(n):
            x = sum = i
            for j in range(m + 1):
                if k >> j & 1:
                    x,s = pa[x][j]
                    sum += s
            res = max(res,sum)
        return res


receiver = [1,1,1,2,3]
k = 3
print(Solution().getMaxFunctionValue(receiver,k))
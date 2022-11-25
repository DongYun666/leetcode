from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        n = len(code)
        code +=code
        if k > 0:
            for i in range(n):
                code[i] = sum(code[i+1:i+k+1])
            return code[0:n]
        else:
            for i in range(len(code)-1,n-1,-1):
                code[i] = sum(code[i+k:i])
            return code[n:]


code = [2,4,9,3]
k = -2
print(Solution().decrypt(code,k))
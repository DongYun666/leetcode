from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A)-1))
        res = 0
        cur = [""] * len(strs)
        for col in zip(*strs):
            temp = cur[:]
            for i, letter in enumerate(col):
                temp[i] = temp[i] + letter
            if is_sorted(temp):
                cur = temp
            else:
                res += 1
        return res

strs = ["cba","daf","ghi"]
strs = ["a","b"]
strs = ["zyx","wvu","tsr"]
strs = ["ca","bb","ac"]
strs = ["xc","yb","za"]
strs = ["xga","xfb","yfa"]
print(Solution().minDeletionSize(strs))
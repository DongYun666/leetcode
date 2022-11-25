class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n>0 and not n&(n-1) else False


n = 0
print(Solution().isPowerOfTwo(n))
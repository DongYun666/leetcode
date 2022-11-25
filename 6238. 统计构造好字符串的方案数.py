class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        res = 0
        candidates = [zero,one]
        def dfs(index, s_m):
            if low<=s_m<=high:
                nonlocal res
                res+=1
            if s_m > high:
                return
            for i in range(len(candidates)):
                s_m += candidates[i]
                dfs(index + 1, s_m)
                s_m -= candidates[i]
        dfs(0, 0)
        return res




low = 2
high = 3
zero = 1
one = 2

# low = 3
# high = 3
# zero = 1
# one = 1
print(Solution().countGoodStrings(low, high, zero, one))

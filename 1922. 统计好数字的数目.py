class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #快速幂
        mod = 10**9+7
        def my_pow(x, N):
            ans = 1
            x_ = x
            while N > 0:
                if N % 2 == 1:
                    ans = ans*x_%mod
                x_ = x_*x_%mod
                N //= 2
            return ans if x>=0 else -1/ans
        odd = n//2+n%2
        even = n//2
        return my_pow(5,odd)*my_pow(4,even) % mod

n = 50
print(Solution().countGoodNumbers(n))


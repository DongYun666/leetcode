class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(x):
            res = 0
            while x != 0:
                res = res * 10 + x % 10
                x //= 10
            return res
        for k in range(num):
            if k+reverse(k) == num:
                return True
        return False

num = 443
print(Solution().sumOfNumberAndReverse(num))
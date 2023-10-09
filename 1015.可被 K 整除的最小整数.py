class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        num = 1
        for i in range(1, k+1):
            if num % k == 0:
                return i,num
            num = num * 10 + 1
        return -1
k = 7
print(Solution().smallestRepunitDivByK(k))



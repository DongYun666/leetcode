class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for x in range(low,high + 1):
            x = str(x)
            if len(x) % 2 == 0:
                pre = sum(int(y) for y in x[:len(x) //2])
                suff = sum(int(y) for y in x[len(x) // 2:])
                if pre == suff:
                    res += 1
                    
        return res
    
low = 1200
high = 1230

low = 1
high = 100
print(Solution().countSymmetricIntegers(low, high))
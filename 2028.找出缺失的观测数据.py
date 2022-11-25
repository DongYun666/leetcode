from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        roll_sum = sum(rolls)
        total = mean*(n+len(rolls))
        res_sum = total - roll_sum
        if mean*n < res_sum:
            return []
        res = [int(res_sum//n)]*n
        if res[0]*n < res_sum:
            for i in range(n):
                res[i]+=1
        print(res)




rolls = [1,5,6]
mean = 3
n = 4
print(Solution().missingRolls(rolls,mean,n))
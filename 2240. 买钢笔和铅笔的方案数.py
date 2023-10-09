
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 1
        if cost2 > cost1:
            cost1,cost2 = cost2,cost1
        for i in range(total//cost1+1):
            if total-i*cost1 >=cost2:
                res += (total-i*cost1)//cost2 if (total-i*cost1)%cost2 else (total-i*cost1)//cost2 + 1
        return res
    


total = 20
cost1 = 10
cost2 = 5

total = 5
cost1 = 10
cost2 = 10

total = 10
cost1 = 9
cost2 = 99
print(Solution().waysToBuyPensPencils(total, cost1, cost2))
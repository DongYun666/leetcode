class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        res = 0
        now = 0
        while now != target:
            res+=1
            if now+res > target:
                now -= res
            else:
                now += res
        return res

target  = 4
print(Solution().reachNumber(target))
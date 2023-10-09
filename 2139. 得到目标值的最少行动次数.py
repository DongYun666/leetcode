class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target!=1:
            if target & 1:
                target -= 1
                res += 1
            elif maxDoubles:
                target //= 2
                maxDoubles -= 1
                res += 1
            else:
                res += target-1
                target = 1
        return res


target = 19
maxDoubles = 2
print(Solution().minMoves(target,maxDoubles))

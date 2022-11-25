from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1+maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal:
            return False
        @cache
        def dfs(usedNumbers,currentTotal):
            for i in range(0,maxChoosableInteger):
                if usedNumbers & 1<<i == 0:
                    if currentTotal+i+1 >= desiredTotal or not dfs(usedNumbers | 1<<i ,currentTotal+i+1):
                        return True
            return False
        return dfs(0,0)

maxChoosableInteger = 10
desiredTotal = 40
print(Solution().canIWin(maxChoosableInteger, desiredTotal))
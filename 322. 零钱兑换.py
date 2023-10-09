from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(total,coins):
            if total == amount:
                return 0
            if total > amount:
                return float("inf")
            res = float("inf")
            for coin in coins:
                res = min(res,dfs(total+coin,coins)+1)
            return res
        res = dfs(0,coins)
        return res if res != float("inf") else -1
coins = [1,2,5]
amount = 11

coins = [2]
amount = 3
print(Solution().coinChange(coins,amount))
from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        # left,right = 0,len(piles)-1
        # while left < right:
        #     res += piles[right-1]
        #     left+=1
        #     right-=2
        for i in range(len(piles)-2,len(piles)//3-1,-2):
            res+=piles[i]
        return res



piles = [9,8,7,6,5,1,2,3,4]
print(Solution().maxCoins(piles))
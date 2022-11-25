from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    res.append(prices[i]-prices[j])
                    break
            else:
                res.append(prices[i])
        return res
# prices = [1,2,3,4,5]
# prices = [8,4,6,2,3]
prices = [8,7,4,2,8,1,7,7,10,1]
print(Solution().finalPrices(prices))

from typing import List
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(price, mid, k):
            pre = float('-inf')
            for i in range(len(price)):
                if price[i] - pre >= mid:
                    k -= 1
                    pre = price[i]
            return k <= 0
        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) >> 1
            if check(price, mid, k):
                left = mid
            else: 
                right = mid - 1
        return left
price = [13,5,1,8,21,2]
k = 3

price = [1,3,1]
k = 2

price = [7,7,7,7]
k = 2
print(Solution().maximumTastiness(price, k))
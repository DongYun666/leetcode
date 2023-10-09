import bisect
from typing import List
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        pre_sum = [0] * (n + 1)
        index = [0] * (n)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + fruits[i - 1][1]
            index[i - 1] = fruits[i - 1][0]
        res = 0
        for x in range(k // 2 + 1):
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect.bisect_left(index, left)
            end = bisect.bisect_right(index, right)
            res = max(res, pre_sum[end] - pre_sum[start])
            y = k - 2 * x 
            left = startPos - y
            right = startPos + x
            start = bisect.bisect_left(index, left)
            end = bisect.bisect_right(index, right)
            res = max(res, pre_sum[end] - pre_sum[start])
        return res
    


fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
startPos = 5
k = 4
print(Solution().maxTotalFruits(fruits, startPos, k))
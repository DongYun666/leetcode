from typing import List
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort(key=lambda x:(x[0],-x[1]))
        n = len(box)
        dp = [0] * n
        for i in range(n):
            dp[i] = box[i][2]
            for j in range(i):
                if box[j][1] <  box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i],dp[j] + box[i][2])
        return max(dp)
box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
print(Solution().pileBox(box))
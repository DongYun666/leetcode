from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            temp_width,j,h = 0,i,0
            while j>0:
                temp_width += books[j-1][0]
                if temp_width>shelfWidth:
                    break
                h = max(h,books[j-1][1])
                dp[i] = min(dp[i],dp[j-1]+h)
                j-=1
        return dp[-1]

books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelf_width = 4
print(Solution().minHeightShelves(books, shelfWidth=shelf_width))
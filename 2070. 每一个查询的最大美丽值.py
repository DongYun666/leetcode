from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def query(target):
            l,r = 0,len(items)
            while l < r:
                mid = (l+r)//2
                if items[mid][0] > target:
                    r = mid
                else:
                    l = mid + 1
            if l == 0:
                return 0
            else:
                return items[l-1][1]
        items.sort()
        n = len(items)
        for i in range(1, n):
            items[i][1] = max(items[i][1], items[i-1][1])
        return [query(q) for q in queries]

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
print(Solution().maximumBeauty(items, queries))
from typing import List

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_ = sum(nums2)
        for query in queries:
            if query[0] == 1:
                for i in range(query[1],query[2]+1):
                    nums1[i] ^= 1
            elif query[0] == 2:
                sum_ += sum(nums1) * query[1]
            else:
                res.append(sum_)
        return res
    
nums1 = [1,0,1]
nums2 = [0,0,0]
queries = [[1,1,1],[2,1,0],[3,0,0]]

nums1 = [1]
nums2 = [5]
queries = [[2,0,0],[3,0,0]]
print(Solution().handleQuery(nums1, nums2, queries))
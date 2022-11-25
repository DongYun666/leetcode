from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(A,B):
            res = []
            while A or B:
                big = A if A>B else B
                res.append(big.pop(0))
            return res

        def select(nums,n):
            res = []
            drop = len(nums)-n
            for num in nums:
                while drop and res and res[-1]<num:
                    res.pop()
                    drop-=1
                res.append(num)
            return res[:n]
        # print(merge(nums1,nums2),nums1,nums2)
        # print(select(nums1,4))
        ans = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                ans.append(merge(select(nums1,i),select(nums2,k-i)))
        # print(ans)
        return max(ans)
#
#
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# print(Solution().maxNumber(nums1, nums2,k))

print([2,2]>[1,2,3])
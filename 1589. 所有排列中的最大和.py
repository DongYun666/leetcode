from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        record = [0]*len(nums)
        for first,end in requests:
            record[first]+=1
            if end+1<len(nums):
                record[end+1]-=1
        for i in range(1,len(record)):
            record[i]+=record[i-1]
        record.sort(reverse=True)
        res = sum(x*y for x,y in zip(nums,record))
        return res % (10**9+7)





nums = [1,2,3,4,5,10]
requests = [[0,2],[1,3],[1,1]]
print(Solution().maxSumRangeQuery(nums, requests))
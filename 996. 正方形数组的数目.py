import math
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        res = 0
        #全排列
        def backtrack(index):
            if index == len(nums):
                nonlocal res
                # if check(nums):
                #     res+=1
                res+=1
                return
            visit = []
            for i in range(index,len(nums)):
                if nums[i] not in visit:
                    visit.append(nums[i])
                    nums[index],nums[i] = nums[i],nums[index]
                    if index>0:
                        temp = nums[index]+nums[index-1]
                        if math.sqrt(temp)%1 == 0:
                            backtrack(index+1)
                    else:
                        backtrack(index+1)
                    nums[index],nums[i] = nums[i],nums[index]
        nums.sort()
        backtrack(0)
        return res

nums = [1,8,17]
# nums = [2,2,2]

print(Solution().numSquarefulPerms(nums))
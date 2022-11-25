from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        temp1,temp2 = [[],[]],[[],[]]
        for i in range(len(nums)):
            temp1[nums[i]%2].append(nums[i])
            temp2[target[i]%2].append(target[i])
        temp1[0].sort()
        temp1[1].sort()
        temp2[0].sort()
        temp2[1].sort()
        res = 0
        for i in range(len(temp1[0])):
            res+=abs(temp1[0][i]-temp2[0][i])
        for i in range(len(temp1[1])):
            res+=abs(temp1[1][i]-temp2[1][i])
        return res//4


nums = [8, 12, 6]
target = [2, 14, 10]

nums = [1,2,5]
target = [4,1,3]
print(Solution().makeSimilar(nums, target))
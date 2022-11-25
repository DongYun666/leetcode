from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        sub_sum = sum(nums) // k
        nums.sort(reverse=True)
        if nums[0]>sub_sum:
            return False

        bucket = [0]*k
        def dfs(index,target,k):
            if index == len(nums):
                return True
            for i in range(k):
                if i>0 and bucket[i] == bucket[i-1]:continue
                if (bucket[i] + nums[index])>target:continue
                bucket[i] += nums[index]
                if dfs(index+1,target,k): return True
                bucket[i] -= nums[index]
            return False
        return dfs(0,sub_sum,k)

nums = [4,3,2,3,5,2,1]
# nums = [4,4,6,2,3,8,10,2,10,7]
k = 4
print(Solution().canPartitionKSubsets(nums,k))
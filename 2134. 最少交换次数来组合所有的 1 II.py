from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        nums+=nums
        res = float("inf")
        def count(num_list):
            for i in range(len(num_list)):
                if num_list[i] == 1:
                    break
            for j in range(len(num_list)-1,-1,-1):
                if num_list[j] == 1:
                    break
            if i<=j:
                return num_list[i:j+1].count(0)
            return 0

        for start in range(n):
            end = start + n
            print(nums[start:end])
            res = min(res,count(nums[start:end]))

        return res
nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
nums = [0,0,0]
nums = [1,1,1]
nums = [1,1,1,0,0,1,0,1,1,0]
print(Solution().minSwaps(nums))
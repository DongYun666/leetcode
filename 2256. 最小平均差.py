from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # 求和
        total_sum = sum(nums)
        n = len(nums)
        pre_sum = 0
        cur_min = float("inf")
        index = -1
        for i in range(n):
            pre_sum += nums[i]
            suf_sum = total_sum - pre_sum
            if i == n-1:
                diff = pre_sum // n
            else:
                diff = abs(pre_sum // (i+1) - suf_sum // (n-i-1))
            if diff < cur_min:
                index = i
                cur_min = diff
        return index



    def minimumAverageDifference1(self, nums: List[int]) -> int:
        # 先求一遍后缀和
        suffix = [nums[-1]]
        for num in nums[-2::-1]:
            suffix = [suffix[0]+num]+suffix
        cur_min = float("inf")
        cur_sum = 0
        index = 0
        for i in range(len(nums)-1):
            cur_sum += nums[i]
            cur_avg = abs(cur_sum//(i+1)-(suffix[i]-nums[i])//(len(nums)-i-1))
            if cur_min > cur_avg:
                index = i
                cur_min = cur_avg
        cur_avg = (cur_sum+nums[-1])//len(nums)
        return index if cur_min <= cur_avg else len(nums)-1




nums = [2, 5, 3, 9, 5, 3]

nums = [0,0,0,0,0]
print(Solution().minimumAverageDifference(nums))
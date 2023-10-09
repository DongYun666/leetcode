from collections import defaultdict
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = [1 if nums[0] else -1]
        for num in nums[1:]:
            diff.append(diff[-1] + (1 if num else -1))
        # 使用字典 计算 diff[i] = diff[j] 的最大距离
        dic = defaultdict(int)
        res = 0
        for i in range(len(diff)):
            if diff[i] not in dic:
                dic[diff[i]] = i
            if diff[i] == 0:
                res = max(res,i+1)
            else:
                res = max(res,i - dic[diff[i]])
        return res

nums = [0,1]
# nums = [0,0,1,1,0,0,0,1]
# nums = [0,0,1]
print(Solution().findMaxLength(nums))
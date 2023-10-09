from collections import Counter
from typing import List
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        # 统计出现次数最多的数字
        counter = Counter(nums)
        most = counter.most_common(1)[0][0]
        mosts = []
        for k,v in counter.items():
            if v == counter[most]:
                mosts.append(k)
        n = len(nums)
        nums = [nums[-1]] + nums + [nums[0]]
        ans = float("inf")
        for most in mosts:
            res = [float("inf")] * (n+2)

            for i in range(1,n+1):
                if nums[i] == most:
                    res[i] = 0
                else:
                    for j in range(n):
                        if nums[j] == most:
                            res[i] = min(res[i],min((i - j + n) % n,(j - i + n ) % n))  
            ans = min(ans,max(res[1:-1]))
        return ans


nums = [2,1,3,3,2]

# nums = [15,14,14,19]

# nums = [1,2,1,2]

# nums = [5,5,5,5]

# nums = [8,8,9,10,9]

nums = [1,11,11,11,19,12,8,7,19]
print(Solution().minimumSeconds(nums))
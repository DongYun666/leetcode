from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        cnt = []
        left = 0
        cur_min_index,cur_max_index = 0,0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                if nums[cur_min_index] == minK and nums[cur_max_index] == maxK:
                    cnt.append([left,cur_min_index,cur_max_index,i])
                else:
                    cur_min_index=cur_max_index=left = i+1
                    continue
            else:
                if nums[i]<=nums[cur_min_index]:
                    cur_min_index = i
                if nums[i]>=nums[cur_max_index]:
                    cur_max_index = i
        if len(cnt) == 0:
            if min(nums)== minK and max(nums)== maxK:
                if cur_min_index>cur_max_index:
                    cur_min_index,cur_max_index = cur_max_index,cur_min_index
                return
            else:
                return 0
        for l,x,y,r in cnt:
            if x>y:
                x,y = y,x
            res+=x-l+r-y
        # print(cnt)
        print(cnt)
        return res


nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5

nums = [1,1,1,1]
minK = 1
maxK = 1

nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
minK = 35054
maxK = 945315
print(Solution().countSubarrays(nums, minK, maxK))
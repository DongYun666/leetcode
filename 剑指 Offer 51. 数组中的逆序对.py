from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def mergeSort(arr,temp,l,r):
            if l < r:
                mid = (l+r)//2
                nonlocal res
                res = mergeSort(arr,temp,l,mid) + mergeSort(arr,temp,mid+1,r)
                i,j,p = l,mid+1,l
                while i <= mid and j<=r:
                    if nums[i] <= nums[j]:
                        temp[p] = nums[i]
                        i+=1
                    else:
                        temp[p] = nums[j]
                        j+=1
                        res += (mid+1-i)
                    p += 1
                for k in range(i,mid+1):
                    temp[p] = nums[k]
                    res += (mid+1-i)
                    p += 1
                for k in range(j,r+1):
                    temp[p] = nums[k]
                    p += 1
                nums[l:r+1] = temp[l:r+1]
                return res
            return 0
        n = len(nums)
        temp = [0] * n
        return mergeSort(nums,temp,0,n-1)

nums = [7,5,6,4]
print(Solution().reversePairs(nums))
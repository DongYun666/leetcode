def quicksort(nums):
    if len(nums) <= 1:
        return nums
    piovt = nums[len(nums) // 2]
    left = [x for x in nums if x < piovt]
    mid = [x for x in nums if x == piovt]
    right = [x for x in nums if x > piovt]
    return quicksort(left) + mid + quicksort(right)

nums = [2,5,7,4,7,0,6,9,7,9,3,5]
print(quicksort(nums))
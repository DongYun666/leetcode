import bisect
#
# queries = [0,1,5,16]
# res = []
# for i in range(len(queries)):
#     t = bisect.bisect_left(nums,queries[i])
#     # if nums[t] == queries[i]:
#     #     res.append(nums[t],nums[t])
#     # else:
#         # if t
#     r = bisect.bisect_right(nums,queries[i])
#     print(t,r)


nums = [1,2,4,6,9,13,14,15]
def bisect_our(nums,target):
    left = -1
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid+1
    return left
print(bisect_our(nums,5))



# print(bisect.bisect(nums,10))
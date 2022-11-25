from collections import defaultdict


def count(nums):
    temp = nums.copy()
    temp.sort()
    mp = defaultdict(int)
    for i in range(len(temp)):
        mp[temp[i]] = i
    loops = 0


    nums.sort()
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    res = 0
    flag = [0 for x in nums]
    for i in range(len(nums)):
        if flag[i] == 0:
            j=i

    print(d)

nums = [7,6,8,5]
       [5,6,7,8]
print(count(nums))
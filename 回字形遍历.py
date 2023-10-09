def traversal(nums):
    res = []
    if not nums:
        return res
    r1,r2 = 0,len(nums)-1
    c1,c2 = 0,len(nums[0])-1
    while r1 <= r2 and c1 <= c2:
        for c in range(c1,c2+1):
            res.append(nums[r1][c])
        for r in range(r1 + 1,r2+1):
            res.append(nums[r][c2])
        if r1 < r2 and c1 < c2:
            for c in range(c2-1,c1,-1):
                res.append(nums[r2][c])
            for r in range(r2,r1,-1):
                res.append(nums[r][c1])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return res


nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(traversal(nums))


def soultion(nums, n, m):
    if all(nums[i] > 0 for i in range(n)) and m >0:
        return False
    if all(nums[i] < 0 for i in range(n)) and m <0:
        return False
    # 从数组中选出一些数，使得他们的和等于m

    def backtrack(nums,target, i, subset):
        if sum(subset) == target:
            return True
        
        if i >= len(nums):
            return False

        # 选择当前元素
        subset.append(nums[i])
        if backtrack(nums,target, i, subset):
            return True
        subset.pop()

        # 不选择当前元素
        return backtrack(nums,target, i+1, subset)
    
    nums = [-i for i in nums]
    nums.sort()
    return backtrack(nums, m ,0,[])

t = int(input())
res_ = []
for _ in range(t):
    n,m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res = soultion(nums, n, m)
    res_.append(res)
print(res_)

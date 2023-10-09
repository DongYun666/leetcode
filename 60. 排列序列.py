
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 采用暴力破解
        nums = [str(i) for i in range(1,n + 1)]
        def dfs(index):
            if index == len(nums):
                k -= 1
                if k == 0:
                    return "".join(nums[:])
            visited = [False] * (n + 1)
            for i in range(index,len(nums)):
                if not visited[nums[i]]:
                    visited[nums[i]] = True
                    nums[index],nums[i] = nums[i],nums[index]
                    dfs(index+1)
                    nums[index],nums[i] = nums[i],nums[index]
        dfs(0)
    
n = 4
k = 9
print(Solution().getPermutation(n, k))



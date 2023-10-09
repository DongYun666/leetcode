class Solution:
    def maxValue1(self, n: int, index: int, maxSum: int) -> int:
        l,r = 1,maxSum-n+1
        while l <= r:
            mid = (l+r)//2
            temp = mid + sum(max(mid-j,1) for j in range(1,index+1))+ sum(max(mid-j,1) for j in range(1,n-index))
            if temp <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res,l,r,temp_sum = 1,index,index,n
        while temp_sum <= maxSum:
            temp_sum += r-l+1
            res += 1
            l = 0 if l == 0 else l-1
            r = n-1 if r == n-1 else r+1
            if l == 0 and r == n-1:
                return res + (maxSum-temp_sum)//n
        return res - 1

n = 6
index = 1
maxSum = 10

# n = 4
# index = 2
# maxSum = 6

# n = 8
# index = 7
# maxSum = 14
print(Solution().maxValue(n, index, maxSum))
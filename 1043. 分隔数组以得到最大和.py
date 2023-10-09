from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        pre = [0] * len(arr)
        suff = [0] * len(arr)
        pre[0] = arr[0]
        suff[0] = arr[-1]
        for i in range(1,len(arr)):
            pre[i] = max(arr[max(0,i - k + 1):i+1])
        print(pre)
        for i in range(len(arr)-1,-1,-1):
            suff[i] = max(arr[i:max(i+k,len(arr))])
        print(suff)
        res = 0
        for i in range(0,len(arr)):
            res += max(pre[i],suff[i])
        return res
arr = [1,15,7,9,2,5,10]
k = 3
print(Solution().maxSumAfterPartitioning(arr,k))

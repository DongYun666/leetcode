import bisect
from typing import List
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        temp = []
        for a in arr:
            if a not in target:
                continue
            else:
                temp.append(target.index(a))
        # 对temp 求最长的连续子序列
        n = len(temp)
        if n == 0:
            return len(target)
        L = [1]*n
        for i in range(1,n):
            for j in range(i):
                if temp[i]>temp[j]:
                    L[i] = max(L[j]+1,L[i])
        return len(target)-max(L)



    def minOperations2(self, target: List[int], arr: List[int]) -> int:
        # 记录target索引编号
        m = len(target)
        dct = dict()
        for i in range(m):
            dct[target[i]] = i
        # 映射arr成索引编号寻找最长递增子序列
        dp = []
        for num in arr:
            if num in dct:
                i = bisect.bisect_left(dp, dct[num])
                if i < len(dp):
                    dp[i] = dct[num]
                else:
                    dp.append(dct[num])
        return m-len(dp)


target = [6, 4, 8, 1, 3, 2]
arr = [4, 7, 6, 2, 3, 8, 6, 1]
print(Solution().minOperations(target, arr))
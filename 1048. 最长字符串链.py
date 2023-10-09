import bisect
from collections import defaultdict
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(first,second):
            cnt = 0
            m = len(second)
            x = 0
            for k in range(m):
                if first[x] == second[k]:
                    x+=1
                else:
                    cnt+=1
                if cnt >= 2:
                    return False
                if x == len(first):
                    break
            return True

        words.sort(key=lambda x: len(x))
        dct = defaultdict(list)
        n = len(words)
        dp = [1] * n
        for i in range(n):
            for j in dct[len(words[i])-1]:
                if check(words[j],words[i]) and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
            dct[len(words[i])].append(i)
        return max(dp)

words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
nums = [1,2,4,5,7,8,10]
# print(bisect.bisect(nums,3)-1)
def biselect(nums,x):
    l,r = 0,len(nums)-1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] <= x:
            l = mid+1
        else:
            r = mid-1
    return l
print(biselect(nums,3))



# print(Solution().longestStrChain(words))
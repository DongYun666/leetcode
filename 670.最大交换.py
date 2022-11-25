class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        res = num
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                s[i],s[j] = s[j],s[i]
                res = max(res,int("".join(s)))
                s[i],s[j] = s[j],s[i]
        return res

num = 2736
print(Solution().maximumSwap(num))
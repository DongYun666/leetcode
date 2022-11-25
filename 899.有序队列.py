class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k != 1:
            return "".join(sorted(s))
        else:
            temp = s+s
            min_ = s
            for i in range(len(s)):
                min_ = min(min_,temp[i:i+len(s)])
            return min_
s = "cba"
k = 1
print(Solution().orderlyQueue(s,k))


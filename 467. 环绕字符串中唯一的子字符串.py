from collections import defaultdict, Counter


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i in range(len(p)):
            if i>0 and (ord(p[i])-ord(p[i-1])+26) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[p[i]] = max(dp[p[i]],k)
        return sum(dp.values())

words = ["i", "love", "leetcode", "i", "love", "coding"]
dect = sorted(Counter(words).items(),key=lambda x: x[1], reverse=True)[:2]
print(dect)


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) < 2:
            return s
        counts = Counter(s)
        max_count = max(counts.items(), key=lambda x: x[1])[1]
        if max_count > (len(s)+1) // 2:
            return ""
        counts = sorted(counts.items(), key=lambda x: x[1])
        res = [""] * len(s)
        odd, even = 1, 0
        for ch, count in counts:
            while count > 0 and odd < len(s):
                count -= 1
                res[odd] = ch
                odd += 2
            while count > 0:
                count -= 1
                res[even] = ch
                even += 2
        return "".join(res)
s = "aab"
print(Solution().reorganizeString(s))
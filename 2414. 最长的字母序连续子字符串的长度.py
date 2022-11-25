class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        stack = []
        t = 0
        res = 0
        for i in range(len(s)):
            if len(stack) == 0 or ord(stack[-1])==ord(s[i])-1:
                t += 1
                res = max(res,t)
            else:
                stack.pop()
                t-=1
            stack.append(s[i])
        return res

enumerate
s = "abacaba"
s = "abcde"
s = "pcfftiovoygwwncfgews"
print(Solution().longestContinuousSubstring(s))
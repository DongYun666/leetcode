class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
s = 'ab**c'
s = "leet**cod*e"
print(Solution().removeStars(s))

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        index = 0
        while index < len(s):
            if s[index] == "(":
                stack.append("(")
                index += 1
            else:
                if index+1 < len(s) and s[index+1] == ")":
                    if stack:
                        stack.pop()
                    else:
                        res += 1
                    index += 2
                else:
                    if stack:
                        stack.pop()
                        res += 1
                    else:
                        res += 2
                    index += 1
        return res + len(stack)*2

s = "))())("
s = "(()))"
print(Solution().minInsertions(s))
        
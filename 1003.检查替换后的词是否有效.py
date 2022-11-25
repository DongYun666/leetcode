class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for w in s:
            if w == "c":
                if len(stack) <2:
                    return False
                b = stack.pop()
                a = stack.pop()
                if b != "b" or a != "a":
                    return False
                continue
            stack.append(w)
        return True if len(stack) == 0 else False

s = "abccba"
# s = "abcabcababcc"
# s = "aabcbc"
# s = "aabbcc"
print(Solution().isValid(s))
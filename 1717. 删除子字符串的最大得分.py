class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # 尽量先寻找大的得分，后找小的得分
        res = 0
        def remove(s,sub,socre):
            stack = []
            for ch in s:
                stack.append(ch)
                while stack and stack[-2:] == list(sub):
                    stack.pop()
                    stack.pop()
                    nonlocal res
                    res += socre
            return "".join(stack)
        
        if x > y:
            s = remove(s,'ab',x)
            s = remove(s,'ba',y)
        else:
            s = remove(s,'ba',y)
            s = remove(s,'ab',x)
        return res

s = "cdbcbbaaabab"

s = "aabbaaxybbaabb"
x = 5
y = 4
print(Solution().maximumGain(s,x,y))
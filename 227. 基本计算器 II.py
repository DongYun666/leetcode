class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        presign = "+"
        for i in range(len(s)):
            if s[i] != ' ' and s[i].isdigit():
                num = num*10+int(s[i])
            if i == len(s)-1 or s[i] in "+-*/":
                if presign == "+":
                    stack.append(int(num))
                elif presign == '-':
                    stack.append(-int(num))
                elif presign == '*':
                    stack.append(int(stack.pop()*int(num)))
                else:
                    stack.append(int(stack.pop()/int(num)))
                presign = s[i]
                num = 0
        return sum(stack)



s = "3+2*2/2"
print(Solution().calculate(s))
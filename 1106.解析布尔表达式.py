class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ",":
                continue
            if c != ")":
                stack.append(c)
                continue
            t,f = 0,0
            while stack[-1]!= "(":
                if stack.pop()== "t":
                    t+=1
                else:
                    f+=1
            stack.pop()
            ex = stack.pop()
            if ex == "!":
                stack.append("t" if f else "f")
            elif ex == "|":
                stack.append("t" if t else "f")
            elif ex == "&":
                stack.append("f" if f else "t")
        return stack[-1] == "t"

expression = "|(&(t,f,t),!(t))"
# expression = "&(t,f)"

expression = "|(f,t)"
expression = "!(f)"
print(Solution().parseBoolExpr(expression))
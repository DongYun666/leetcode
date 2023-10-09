class Solution:
    def checkValidString(self, s: str) -> bool:
        temp = []
        for c in s:
            if c == "(" or c == "*":
                temp.append(c)
            else:
                # 尽可能的将* 视为字符串，不进行匹配
                if len(temp) == 0:
                    return False
                for i in range(len(temp)-1,-1,-1):
                    if temp[i] == "(":
                        break
                temp.pop(i)
        count = 0
        for i in range(len(temp)-1,-1,-1):
            if temp[i] == "*":
                count +=1
            else:
                if count == 0:
                    return False
                else:
                    count -=1
        return  True




s = "(*))"
s = "(*)))"
# s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
# s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
print(Solution().checkValidString(s))

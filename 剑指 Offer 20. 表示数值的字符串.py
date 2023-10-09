class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去除首尾空格
        num, dot, exp, sign = False, False, False, False
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = True
            elif s[i] == '.' and not dot and not exp:
                dot = True
            elif (s[i] == 'e' or s[i] == 'E') and not exp and num:
                exp, num, sign = True, False, False
            elif (s[i] == '+' or s[i] == '-') and not sign and (i == 0 or s[i - 1] == 'e' or s[i - 1] == 'E'):
                sign = True
            else:
                return False
        return num
s = "1 "
print(Solution().isNumber(s))

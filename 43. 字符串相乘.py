class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m,n = len(num1)-1,len(num2)-1
        res = ""
        temp = 0
        while m >= 0 or n >= 0:
            x = int(num1[m]) if m >= 0 else 0
            y = int(num2[n]) if n >= 0 else 0
            temp = x + y + temp
            res = str(temp%10) + res
            temp = temp//10
            m -= 1
            n -= 1
        if temp > 0:
            res = str(temp) + res
        return res
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':return '0'
        m,n = len(num1)-1,len(num2)-1
        res = ""
        while n >= 0:
            x = num2[n]
            temp = 0
            mul = ""
            while m >= 0:
                y = int(num1[m])*int(x) + temp
                mul = str(y%10) + mul
                temp = y//10
                m -= 1
            if temp > 0:
                mul = str(temp) + mul
            res = self.addStrings(res,mul+"0"*(len(num2)-n-1))
            n -= 1
            m = len(num1)-1
        return res
num1 = "123"
num2 = "456"

num1 = "408"
num2 = "5"

num1 = "123456789"
num2 = "987654321"

num1 = "2"
num2 = "3"
print(Solution().multiply(num1,num2))
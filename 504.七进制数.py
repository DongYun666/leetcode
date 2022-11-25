# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 9:38
# @Author : DongYun
# @File : 504.七进制数.py
# @Software : PyCharm
class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = True
        ans  =  ""
        if num == 0:
            return "0"
        if num<0:
            flag = False
            num = abs(num)
        while num !=0:
            ans+=str(num%7)
            num //=7
        return "".join(reversed(list(ans))) if flag else  "-"+"".join(reversed(list(ans)))
num = 0
print(Solution().convertToBase7(num))



# -*- codeing = utf-8 -*-
# @Time : 2022/2/23 13:55
# @Author : DongYun
# @File : 917.仅仅反转字母.py
# @Software : PyCharm
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)

        left,right = 0, len(s)-1
        while True:
            while left < right and not ans[left].isalpha():
                left+=1
            while left < right and not ans[right].isalpha():
                right -=1
            if left>=right:
                break
            ans[left],ans[right] = ans[right],ans[left]
            left+=1
            right-=1
        return "".join(ans)

        return ans


s = "a-bC-dEf-ghIj"
print(Solution().reverseOnlyLetters(s))


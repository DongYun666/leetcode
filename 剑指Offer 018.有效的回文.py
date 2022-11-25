# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 10:40
# @Author : DongYun
# @File : 剑指Offer 018.有效的回文.py
# @Software : PyCharm

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for ch in s:
            if ch.isalpha() or ch.isalnum():
                temp+=ch.lower()
        i,j = 0,len(temp)-1
        while i<j:
            if temp[i] != temp[j]:
                return False
            else:
                i+=1
                j-=1
        return True
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
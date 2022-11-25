# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 20:37
# @Author : DongYun
# @File : HJ32 密码截取.py
# @Software : PyCharm

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longestPalindrome(s) -> str:
    maxlength = 1
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        maxlength = max(max(maxlength, right1 - left1 + 1),right2 - left2 + 1)
    return maxlength
while True:
    try:
        s = input()
        print(longestPalindrome(s))
    except:
        break
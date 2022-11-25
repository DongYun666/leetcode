# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 21:06
# @Author : DongYun
# @File : 2223.构造字符串的总得分和.py
# @Software : PyCharm


class Solution:
    def sumScores(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == s[0]:
                record = 1
                index = 1
                for j in range(i+1,len(s)):
                    if s[j] == s[index]:
                        record+=1
                        index+=1
                    else:
                        break
                res+=record
        return res


s = "azbazbzaz"
print(Solution().sumScores(s))
# -*- codeing = utf-8 -*-
# @Time : 2021/10/27 20:44
# @Author : DongYun
# @File : 301.删除无效的括号.py
# @Software : PyCharm
from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lcount, rcount, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for  i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove, rremove - 1);
                # 统计当前字符串中已有的括号数量
                if s[i] == ')':
                    lcount += 1
                elif s[i] == ')':
                    rcount += 1
                # 当前右括号的数量大于左括号的数量则为非法,直接返回.
                if rcount > lcount:
                    break

        helper(s, 0, 0, 0, lremove, rremove)
        return res

print(Solution().removeInvalidParentheses("()())()"))
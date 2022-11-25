# -*- codeing = utf-8 -*-
# @Time : 2021/12/3 17:24
# @Author : DongYun
# @File : 剑指 Offer 67.把字符串转换成整数.py
# @Software : PyCharm
class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        ans = 0
        flag = False
        for s in str:
            x = ord(s) - 48

            if x == -3:
                flag = True
            elif 0<=x<=9:
                ans = ans*10+x
            elif x != -5:
                break
        return max(-ans,-2**31) if flag else min(ans,2**31-1)

    def strToInt1(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str)
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if not str: return 0  # 空字符串，提前返回
        while str[i] == ' ':
            i += 1
            if i == length: return 0  # 字符串全为空格，提前返回
        if str[i] == '-': sign = -1
        if str[i] in '+-': i += 1
        for c in str[i:]:
            if not '0' <= c <= '9': break
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res


print(Solution().strToInt1("+-1"))
# -*- codeing = utf-8 -*-
# @Time : 2022/3/25 15:12
# @Author : DongYun
# @File : 172.阶乘后的零.py
# @Software : PyCharm


class Solution:
    def trailingZeroes(self, n: int) -> int:
        dict = {125:1,625:2,3125:3}
        count = (n // 5)
        count+=count//5
        for x in dict.keys():
            if n >= x:
                count+=dict[x]
        return count

    def trailingZeroes2(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


n = 268
print(Solution().trailingZeroes2(n))

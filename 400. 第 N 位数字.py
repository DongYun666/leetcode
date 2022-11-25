# -*- codeing = utf-8 -*-
# @Time : 2021/11/30 10:15
# @Author : DongYun
# @File : 400. 第 N 位数字.py
# @Software : PyCharm

class Solution:


    def findNthDigit2(self, n: int) -> int:
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10

    def findNthDigit3(self,n:int) -> int:
        len = 1
        while len*9*10**(len-1) < n:
            n-= len*9*10**(len-1)
            len+=1
        s = 10 ** (len-1)
        x = int(n / len) +s -1
        n-=(x-s+1)*len
        return int(x%10) if n == 0 else (x+1)/(10**(len-n)%10)



print(Solution().findNthDigit3(10))
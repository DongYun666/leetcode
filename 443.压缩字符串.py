# -*- codeing = utf-8 -*-
# @Time : 2022/3/24 18:03
# @Author : DongYun
# @File : 443.压缩字符串.py
# @Software : PyCharm

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = 0
        right = 0
        for index in range(len(chars)):
            right = index+1
            while right < len(chars) and chars[right] == chars[index]:
                right+=1
            length = right - index
            if length == 1:
                chars.insert(cur+1,length)
                cur+=2
            else:
                while

            index+=length









    # def compress(self, chars: List[str]) -> int:
    #     def reverse(left: int, right: int) -> None:
    #         while left < right:
    #             chars[left], chars[right] = chars[right], chars[left]
    #             left += 1
    #             right -= 1
    #
    #     n = len(chars)
    #     write = left = 0
    #     for read in range(n):
    #         if read == n - 1 or chars[read] != chars[read + 1]:
    #             chars[write] = chars[read]
    #             write += 1
    #             num = read - left + 1
    #             if num > 1:
    #                 anchor = write
    #                 while num > 0:
    #                     chars[write] = str(num % 10)
    #                     write += 1
    #                     num //= 10
    #                 reverse(anchor, write - 1)
    #             left = read + 1
    #     return write


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print((Solution().compress(chars)))

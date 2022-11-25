# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 19:59
# @Author : DongYun
# @File : 744. 寻找比目标字母大的最小字母.py
# @Software : PyCharm

from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0]:
            return letters[0]
        if target >=letters[-1]:
            return letters[0]
        left,right = 0 , len(letters)-1
        while left < right-1:
            mid = (left + right)>>1
            if letters[mid]>target:
                right = mid
            else:
                l = mid
        if letters[l] > target:
            return letters[l]
        else:
            return letters[l+1]



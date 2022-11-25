# -*- codeing = utf-8 -*-
# @Time : 2022/3/31 10:52
# @Author : DongYun
# @File : 728.自除数.py
# @Software : PyCharm
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def compute(x):
            temp = x
            while x!= 0:
                a = x%10
                if a ==0  or temp % a != 0 :
                    return False
                x //=10
            return True
        return [i for i in range(left,right+1) if compute(i)]


print(Solution().selfDividingNumbers(1,22))

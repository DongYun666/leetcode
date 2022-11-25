# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 19:16
# @Author : DongYun
# @File : 6055.转化时间需要的最少操作数.py
# @Software : PyCharm


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = int(current.split(":")[0])
        current_sec = int(current.split(":")[1])
        correct_time = int(correct.split(":")[0])
        correct_sec = int(correct.split(":")[1])
        couont_time = 60*(correct_time-current_time)+correct_sec-current_sec
        res = 0
        for num in [60,15,5,1]:
            res += couont_time//num
            couont_time %= num
        return res

current = "02:30"
correct = "04:35"
print(Solution().convertTime(current,correct))

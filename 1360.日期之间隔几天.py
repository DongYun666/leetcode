# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 10:45
# @Author : DongYun
# @File : 1360.日期之间隔几天.py
# @Software : PyCharm

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split("-")
        date2 = date2.split("-")
        return 365*(int(date2[0])-int(date1[1]))
        return 0

date1 = "2019-06-29"
date2 = "2019-06-30"
print(Solution().daysBetweenDates(date1,date2))

# -*- codeing = utf-8 -*-
# @Time : 2022/3/22 17:38
# @Author : DongYun
# @File : 2086. 从房屋收集雨水需要的最少水桶数.py
# @Software : PyCharm


class Solution:
    def minimumBuckets(self, street: str) -> int:
        count = 0
        street = list(street)
        for index,s in enumerate(street):
            if s != "H":continue
            if s == "H" and index -1 >= 0 and street[index-1] == "B":continue
            if s == "H" and index+1 < len(street) and street[index+1] == ".": #遇到房屋先往右边放一只桶
                count+=1
                street[index+1] = "B" #标记已经放置桶
            elif index -1 >=0 and street[index-1] == ".":
                count+=1
                street[index-1] = "B"
            else:
                return -1

        return count


street = ".H.H."
print(Solution().minimumBuckets(street))
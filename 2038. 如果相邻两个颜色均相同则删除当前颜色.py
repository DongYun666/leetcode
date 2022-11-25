# -*- codeing = utf-8 -*-
# @Time : 2022/3/22 16:56
# @Author : DongYun
# @File : 2038. 如果相邻两个颜色均相同则删除当前颜色.py
# @Software : PyCharm

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        temp = [0,0]
        cnt = 1
        cur = colors[0]
        for i in range(1,len(colors)):
            if cur == colors[i]:
                cnt+=1
                if cnt>=3:
                    temp[ord(cur) - ord("A")]+=1
            else:
                cnt = 1
                cur = colors[i]
        return temp[0] > temp[1]

colors = "AAABABBAAA"
print(Solution().winnerOfGame(colors))


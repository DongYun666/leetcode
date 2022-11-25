# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 19:59
# @Author : DongYun
# @File : 测试动态规划.py
# @Software : PyCharm
aim = 10
arr = [2, 5, 1,1, 1]
def func():
    dp = [[0 for col in range(len(arr) + 1)] for row in range(max(arr) + aim)]
    for i in range(len(arr)+1):
        dp[aim][i] = 1
    for i in range(len(arr)-1,-1,-1):
        for j in range(aim):
            dp[j][i] = dp[j+arr[i]][i+1]+dp[j][i+1]
    print(dp)
    return dp[7][0]
print(func())
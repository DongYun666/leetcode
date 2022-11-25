# -*- codeing = utf-8 -*-
# @Time : 2022/7/24 13:25
# @Author : DongYun
# @File : Path.py
# @Software : PyCharm
n = int(input())
ditu = []
for _ in range(n):
    temp = list(map(str, input()))
    ditu.append(temp)
count = float("inf")
def path(ditu,i,j,count):
    ditu_temp = ditu.copy()
    if 0<=i<n and 0<=j<n:
        #往右走
        if ditu_temp[i][j] =='N':
            count += 1
            return count
        else:
            ditu_temp[i][j] = 'N'
        return max(max(path(ditu_temp,i+1,j,count),path(ditu_temp,i,j+1,count)),max(path(ditu_temp,i-1,j,count),path(ditu_temp,i,j-1,count)))
    else:
        return count

for i in range(n):
    for j in range(n):
        if ditu[i][j] == 'P':
            count = min(count,path(ditu,i,j,0))
print(count)
# -*- codeing = utf-8 -*-
# @Time : 2022/4/10 10:05
# @Author : DongYun
# @File : 海洋和土地.py
# @Software : PyCharm

from typing import List
class Solution:
    def test(self,x:List[List[int]]):
        flag_left = False
        flag_right = False
        for i in x:
            if len(i) == 0:
                continue
            left = i[0:i.index(max(i))]
            left_ = sorted(left)
            left_reverse = left_.reverse()
            right = i[i.index(max(i)):len(i)]
            right_ = sorted(right)
            right_reverse = right_.reverse()
            if left == left_ :
                flag_left = True
            if left == left_reverse:
                flag_left = True
            if right == right_:
                flag_right = True
            if right == right_reverse:
                flag_right = True
            if not flag_left or not flag_right:
                break
        return 1 if flag_left and flag_right else 0
if __name__ == '__main__':
    T = int(input())
    ans = []
    while T!= 0:
        res = []
        temp = []
        T-=1
        x = int(input())
        while x!= 0:
            k = list(map(eval,input().split()))
            k_i = k[0]
            temp = k[1:len(k)]
            x-=1
            res.append(temp)
        ans.append(Solution().test(res))
    print(ans)


# 2
# 1
# 1 1
# 2
# 5 5 4 3 2 1
# 4 9 6 7 8



# 1
# 2
# 5 5 4 3 2 1
# 4 9 6 7 8

# 1
# 3
# 0
# 5 1 2 5 4 3
# 4 6 9 8 7
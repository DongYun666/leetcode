# -*- codeing = utf-8 -*-
# @Time : 2022/3/8 16:33
# @Author : DongYun
# @File : 2055. 蜡烛之间的盘子.py
# @Software : PyCharm
import bisect
from typing import List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        temp = {}
        count = 0
        flag = False
        for index,c in enumerate(s):
            if not flag and c == "|":
                flag = True
            if flag and c == "*":
                count+=1
            if flag and c == "|":
                temp[index] = count
        # # //使用二分查找
        temp_key = list(temp.keys())
        for query in queries:
            left = query[0]
            right = query[1]
            candle_left = bisect.bisect_left(temp_key, left)
            candle_right = bisect.bisect_right(temp_key, right) - 1
            res.append((temp[temp_key[candle_right]] - temp[temp_key[candle_left]])if candle_right > candle_left else 0)
        return res


    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l
        print(preSum)
        print(left)
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r
        print(right)
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans

    def platesBetweenCandles3(self, s: str, queries: List[List[int]]) -> List[int]:
        # 获取蜡烛的位置
        candles = [i  for i in range(len(s)) if s[i]=='|']
        # print(candles)

        res = []
        for left, right in queries:
            candle_left = bisect.bisect_left(candles, left)
            candle_right = bisect.bisect_right(candles, right) - 1
            # print(candle_right, candle_left)

            # 两个蜡烛中间可能还会有蜡烛，蜡烛个数为 candle_right - candle_left
            res.append(candles[candle_right] - candles[candle_left] - (candle_right - candle_left)
                        if candle_right > candle_left else 0)

        return res



s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
print(Solution().platesBetweenCandles(s,queries))


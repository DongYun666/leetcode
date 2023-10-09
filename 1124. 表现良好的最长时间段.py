from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        temp = [0] * n
        temp[0] = 1 if hours[0] > 8 else -1
        for i,hour in enumerate(hours[1:],1):
            temp[i] = temp[i-1] + (1 if hour > 8 else -1)
        # 求 1 最后一次出现的位置
        for i in range(n-1,-1,-1):
            if temp[i] == 1:
                return i+1
        return 0
hours = [9,9,6,0,6,6,9]
hours = [6,6,6]
print(Solution().longestWPI(hours))
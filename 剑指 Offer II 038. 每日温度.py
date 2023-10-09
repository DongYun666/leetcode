from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index,temperatur in enumerate(temperatures):
            while stack and temperatur>stack[-1][0]:
                res[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append([temperatur,index])
        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
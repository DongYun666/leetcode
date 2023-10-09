from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #使用栈
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                temperatures[index] = i - index
            stack.append(i)
        while stack:
            temperatures[stack.pop()] = 0
        return temperatures
    
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
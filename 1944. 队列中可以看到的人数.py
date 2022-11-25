from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0]*len(heights)
        for i in range(len(heights)):
            stack = []
            for j in range(i+1,len(heights)):
                if heights[j] >= heights[i]:
                    stack.append(heights[j])
                    break
                else:
                    if len(stack) == 0:
                        stack.append(heights[j])
                    elif stack[-1]<heights[j]:
                        stack.append(heights[j])
            res[i] = len(stack)
        return res


heights = [10, 6, 8, 5, 11, 9]

heights = [5,1,2,3,10]
print(Solution().canSeePersonsCount(heights))
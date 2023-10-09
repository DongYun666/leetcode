from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return j == len(popped)

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

popped = [4,3,5,1,2]
print(Solution().validateStackSequences(pushed, popped))
from turtle import circle
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0, len(citations)
        while left<right:
            mid = (left+right) // 2
            if citations[mid]<len(citations)-left:
                left+=1
            else:
                right-=1
        return len(citations) - left
citations = [0,1,3,5,6]
print(Solution().hIndex(citations))













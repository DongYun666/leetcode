from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i,box in enumerate(boxes):
            res.append(sum(abs(j-i) for j,c in enumerate(boxes) if c == "1"))
        return res

boxes = "110"
print(Solution().minOperations(boxes))
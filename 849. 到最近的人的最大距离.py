from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [0]
        right = [0]
        for i in range(len(seats)):
            if seats[i] == 1:
                left.append(0)
            else:
                left.append(left[-1]+1)
        for j in range(len(seats)-1,-1,-1):
            if seats[j] == 1:
                right = [0] + right
            else:
                right = [right[0]+1] + right
        left = left[1:]
        right = right[:-1]
        res = []
        for i in range(len(left)):
            if i == 0 or i == len(left)-1:
                res.append(max(right[i],left[i]))
            else:
                res.append(min(right[i],left[i]))
        return max(res)

seats = [0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]
print(Solution().maxDistToClosest(seats))
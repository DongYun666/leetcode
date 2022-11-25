from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i,j = 0,len(plants)-1
        cnt = 0
        a,b = capacityA,capacityB
        while i<j:
            if a>=plants[i]:
                a-=plants[i]
            else:
                a = capacityA-plants[i]
                cnt+=1
            if b>=plants[j]:
                b-=plants[j]
            else:
                b = capacityB-plants[j]
                cnt+=1
            i+=1
            j-=1
        if i == j and max(a,b) < plants[i]:
            cnt+=1
        return cnt

plants = [2, 2, 3, 3]
capacityA = 3
capacityB = 4

# plants = [2,2,3,3]
# capacityA = 5
# capacityB = 5

# plants = [5]
# capacityA = 10
# capacityB = 8

# plants = [1,2,4,4,5]
# capacityA = 6
# capacityB = 5

# plants = [7,7,7,7,7,7,7]
# capacityA = 8
# capacityB = 7
print(Solution().minimumRefill(plants, capacityA, capacityB))
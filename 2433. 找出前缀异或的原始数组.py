from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res  = [pref[0]]
        for i in range(1,len(pref)):
            res.append(pref[i] ^ pref[i-1])
        return res
    
pref = [5,2,0,3,1]
pref = [13]
print(Solution().findArray(pref))

from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        recordr = [0,0,0]
        for b in bills:
            if b == 5:
                recordr[0]+=1
            elif b == 10:
                if recordr[0] == 0:
                    return False
                else:
                    recordr[0]-=1
                    recordr[1]+=1
            elif b == 20:
                if recordr[0]*5 + recordr[1]*10 <15 or recordr[0] == 0:
                    return False
                else:
                    if recordr[1] !=0:
                        recordr[1]-=1
                        recordr[0]-=1
                    else:
                        recordr[0]-=3

        return True

bills = [5,5,10,10,20]
print(Solution().lemonadeChange(bills))
from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = []
        for beam in bank:
            cnt = beam.count("1")
            if cnt == 0:
                continue
            temp.append(cnt)
        pre = 0
        res = 0
        for cnt in temp:
            res += pre * cnt
            pre = cnt
        return res
        


bank = ["011001","000000","010100","001000"]
print(Solution().numberOfBeams(bank))
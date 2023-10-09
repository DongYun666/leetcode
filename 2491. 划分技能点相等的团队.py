from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        temp = skill[0] + skill[-1]
        res = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i-1] != temp:
                return -1
            res += skill[i] * skill[-i-1]
        return res
skill = [3,2,5,1,3,4]
skill = [3,4]
skill = [1,1,2,3]
print(Solution().dividePlayers(skill))
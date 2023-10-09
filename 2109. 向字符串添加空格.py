from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        s_index = 0
        index = 0
        res = ""
        for c in s:
            if s_index<len(spaces) and index == spaces[s_index]:
                res += " "
                s_index +=1
                index += 1
            else:
                index += 1
            res+=c
        return res


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

s = "icodeinpython"
spaces = [1,5,7,9]
print(Solution().addSpaces(s,spaces))
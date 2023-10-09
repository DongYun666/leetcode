from typing import List

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def dfs(i1,i2,length):
            if length == 1:
                return s1[i1] == s2[i2]
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True
            if sorted(s1[i1:i1+length]) != sorted(s2[i2:i2+length]):
                return False
            for i in range(1,length):
                if dfs(i1,i2,i) and dfs(i1+i,i2+i,length-i):
                    return True
                if dfs(i1,i2 + length - i , i) and dfs(i1 + i,i2,length - i):
                    return True
            return False
        return dfs(0,0,len(s1))

s1 = "great"
s2 = "rgeat"

s1 = "abcde"
s2 = "caebd"
print(Solution().isScramble(s1, s2))
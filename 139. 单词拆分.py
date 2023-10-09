from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(index,temp):
            t = "".join(temp)
            if index >= len(wordDict) or len(t)>len(s):
                return False
            if t == s:
                return True
            for i in range(index,len(wordDict)):
                return dfs(index+1,temp.append(wordDict[i])) or dfs(index+1,temp)
        return dfs(0,[])

s = "applepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))

s = ["1","2","3"]
print("".join(s))
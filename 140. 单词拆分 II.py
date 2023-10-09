from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from collections import defaultdict
        dict = defaultdict(list)
        for word in wordDict:
            dict[word[0]].append(word)
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(' '.join(path))
                return
            for word in dict[s[i]]:
                if s[i:i+len(word)] == word:
                    dfs(i+len(word), path+[word])
        dfs(0, [])
        return res

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(Solution().wordBreak(s, wordDict))
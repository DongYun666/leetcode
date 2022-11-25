from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def count(word):
            temp = [0]*52
            for i,w in enumerate(word):
                temp[ord(w)-ord("a")+26*(i%2)]+=1
            return tuple(temp)
        res = set(count(word) for word in words)
        return len(res)

words = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
print(Solution().numSpecialEquivGroups(words))
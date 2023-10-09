from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import defaultdict
        dict = defaultdict(int)
        for word in words2:
            for char in word:
                dict[char] = max(dict[char], word.count(char))
        res = []
        for word in words1:
            for char in dict:
                if word.count(char) < dict[char]:
                    break
            else:
                res.append(word)
        return res
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
print(Solution().wordSubsets(words1, words2))

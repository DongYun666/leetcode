from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1)=="".join(word2)



word1 = ["ab", "c"]
word2 = ["a", "bc"]

word1 = ["a", "cb"]
word2 = ["ab", "c"]

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(Solution().arrayStringsAreEqual(word1, word2))
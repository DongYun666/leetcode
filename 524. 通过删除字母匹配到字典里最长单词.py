from collections import defaultdict
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x),x))
        # 判断word 是否是s的子串
        def check(s_,word):
            if word == s_:
                return True
            if len(word) > len(s_):
                return False
            i,j = 0,0
            while i < len(word) and j < len(s_):
                if s_[j] == word[i]:
                    i+=1
                j+=1
            return True if i == len(word) else False
        for word in dictionary:
            if check(s,word):
                return word
        return ""

s = "abpcplea"
dictionary = ["ale","apple", "monkey", "plea"]

# s = "abpcplea"
# dictionary = ["a","b","c"]
print(Solution().findLongestWord(s, dictionary))


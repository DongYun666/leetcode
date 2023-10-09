from itertools import accumulate
from typing import List
class Solution:
    # def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    #     vowels = {'a', 'e', 'i', 'o', 'u'}
    #     count = [0]*len(words)
    #     def checkVowels(word):
    #         return word[0] in vowels and word[-1] in vowels
    #     count[0] = int(checkVowels(words[0]))
    #     for i,word in enumerate(words[1:],1):
    #         count[i] = count[i-1] + int(checkVowels(word))
    #     res = [0] * len(queries)
    #     for i,(l,r) in enumerate(queries):
    #         res[i] = count[r] - count[l-1] if l > 0 else count[r]
    #     return res
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = list(accumulate((w[0] in "aeiou" and w[-1] in "aeiou" for w in words), initial=0))
        print(s)
        return [s[r + 1] - s[l] for l, r in queries]


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
print(Solution().vowelStrings(words, queries))
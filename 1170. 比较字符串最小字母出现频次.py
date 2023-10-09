import bisect
from typing import List
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        w = sorted([f(i) for i in words])
        return [len(w) - bisect.bisect(w, f(i)) for i in queries]

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(Solution().numSmallerByFrequency(queries, words))
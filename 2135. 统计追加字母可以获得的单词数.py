from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def mask(word: str) -> int:
            res = 0
            for ch in word:
                res |= 1<<(ord(ch) - ord('a'))
            return res
        masks = set()
        for start in startWords:
            msk = mask(start)
            for i in range(26):
                if((msk >> i) & 1) == 0:
                    masks.add(msk | (1 << i))
        cnt = 0
        for target in targetWords:
            if (mask(target) in masks):
                cnt += 1
        return cnt 
    
startWords = ["ant","act","tack"]
targetWords = ["tack","act","acti"]
print(Solution().wordCount(startWords, targetWords))
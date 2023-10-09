from collections import Counter
from functools import lru_cache
from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target = Counter(target)
        stickers = [Counter(sticker) & target for sticker in stickers]
        res = float("inf")
        @lru_cache(None)
        def dfs(index,cur):
            if index == len(stickers):
                return 0 if not cur else float("inf")




        # print(stickers)
        # print(target)

stickers = ["with","example","science"]
target = "thehat"
print(Solution().minStickers(stickers,target))
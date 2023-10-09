class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        tiles = list(tiles)
        from collections import Counter
        counter = Counter(tiles)
        res = 0
        def dfs(counter):
            nonlocal res
            for key in counter:
                if counter[key] > 0:
                    res += 1
                    counter[key] -= 1
                    dfs(counter)
                    counter[key] += 1
        dfs(counter)
        return res
tiles = "AAB"
print(Solution().numTilePossibilities(tiles))
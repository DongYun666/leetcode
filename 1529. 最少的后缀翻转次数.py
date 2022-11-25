class Solution:
    def minFlips(self, target: str) -> int:
        cur = "0"
        res = 0
        for t in target:
            if t == cur:
                continue
            else:
                res += 1
                cur = "0" if cur == "1" else "1"
        return res

target = "10111"
print(Solution().minFlips(target))
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = right = maxn = 0
        n = len(s)
        while right < n:
            d[s[right]] += 1
            maxn = max(maxn, d[s[right]])
            if right - left + 1 - maxn > k:
                d[s[left]] -= 1
                left += 1
            right += 1
        return right - left
s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))
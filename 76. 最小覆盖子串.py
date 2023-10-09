from collections import Counter, defaultdict


class Solution:
    def check(self, count_s, count_t):
        for key in count_t:
            if count_s[key] < count_t[key]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        res = ""
        min_len = float("inf")
        left = 0
        
        for right in range(len(s)):
            count_s[s[right]] += 1
            while self.check(count_s, count_t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                count_s[s[left]] -= 1
                left += 1
        return res
    
s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "aa"
print(Solution().minWindow(s, t))    
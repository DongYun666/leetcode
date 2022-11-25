from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        cnt = defaultdict(int)
        res = 1
        end = -1
        for start in range(len(s)):
            if start!=0:
                cnt.pop(s[start-1])
            while end+1 < len(s) and not cnt.get(s[end+1],None):
                cnt[s[end+1]] = 1
                end+=1
            res = max(res,end-start+1)
        return res



s = "pwwkew"
# s = "abcabcbb"
# s = "bbbbbbb"
# s = " "
# s = ""
# s = "au"
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
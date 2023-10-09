class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        counts = [0]*26
        for i in range(len(s)):
            counts[(ord(t[i]) - ord(s[i]) + 26) % 26] += 1
        for change,count in enumerate(counts[1:],1):
            if change+26*(count-1) > k:
                return False
        return True

s = "input"
t = "ouput"
k = 9

# s = "aab"
# t = "bbb"
# k = 27
print(Solution().canConvertString(s, t, k))


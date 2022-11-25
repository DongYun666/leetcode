class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        while len(s) != 1 and len(s)!=0 and s[0] == s[-1]:
            left,right = 0,len(s)-1
            while s[left] == s[left + 1] and left+1 < right:
                left+=1
            while s[right] == s[right - 1] and left+1 < right:
                right-=1
            s = s[left+1:right]

        return len(s)
s = "ca"
print(Solution().minimumLength(s))
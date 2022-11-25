class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        index,length_s,last,ans = 0,len(s),0,0
        while index<length_s:
            s_i = s[index]
            count = 0
            while index<length_s and s_i == s[index]:
                count+=1
                index+=1
            ans += min(count,last)
            last = count
        return ans

s = '10101'
print(Solution().countBinarySubstrings(s))
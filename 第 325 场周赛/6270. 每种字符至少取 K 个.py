from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 把连个字符串合并起来，求最短的子字符串中同时包含 a,b,c 各k个 的长度
        a_k=b_k=c_k=0
        res = len(s)
        i,j = 0,0
        s+=s
        while j < len(s):
            while j < len(s) and (a_k < k or b_k < k or c_k < k):
                if s[j] == "a":
                    a_k += 1
                if s[j] == "b":
                    b_k += 1
                if s[j] == "c":
                    c_k += 1
                j+=1
            while i<j and a_k >= k and b_k>=k and c_k>=k:
                res = min(res, j - i)
                if s[i] == "a":
                    a_k -= 1
                if s[i] == "b":
                    b_k -= 1
                if s[i] == "c":
                    c_k -= 1
                i+=1

        return res if i!=0 else -1

s = "aabaaaacaabc"
k = 2

s = "a"
k = 0
print(Solution().takeCharacters(s,k))
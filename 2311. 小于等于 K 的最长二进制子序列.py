class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        temp = []
        def count(s_):
            ans = 0
            for i in range(len(s_) - 1, -1, -1):
                ans += int(s_[i]) * 2 ** (len(s_) - i - 1)
            return ans
        def dfs(index):
            if index == len(s):
                t = "".join(temp)
                if count(t)<=k:
                    nonlocal res
                    res = max(res,len(t))
                return
            #选择：
            temp.append(s[index])
            dfs(index+1)
            temp.pop()
            dfs(index+1)
        dfs(0)
        return res
s = "1001010"
k = 5

s = "00101001"
k = 1
print(Solution().longestSubsequence(s,k))
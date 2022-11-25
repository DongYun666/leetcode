from collections import defaultdict


class Solution:
    def numberOfSubstrings1(self, s: str) -> int:

        res = []
        temp = []
        def dfs(index,s):
            if index == len(s):
                if "a" in temp and "b" in temp and "c" in temp:
                    res.append(temp[:])
                return
            temp.append(s[index])
            dfs(index+1,s)
            temp.pop()
            dfs(index+1,s)
        dfs(0,s)
        return res
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = defaultdict(int)
        count["a"] = count["b"] = count["c"] = 0
        start = 0
        for end in range(len(s)):
            count[s[end]]+=1
            while count["a"]>0 and count["b"]>0 and count["c"]>0:
                res+=len(s)-end
                count[s[start]]-=1
                start+=1
        return res





s = "abcabc"
s = "aaacb"
s = "abaaa"
print(Solution().numberOfSubstrings(s))
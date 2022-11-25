from collections import Counter


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        s = list(s)
        ans = []
        temp = []
        res = 0
        #求唯一字符的个数
        def count(s):
            res = 0
            s = Counter(s)
            for x in s:
                if s[x] == 1:
                    res +=1
            return res
        # 求子集
        def dfs(cur):
            if cur == len(s):
                nonlocal res
                res+=count(temp[:])
                print(temp[:])
                print(res)
                # ans.append(temp[:])
                return
            temp.append(s[cur])
            dfs(cur + 1)
            temp.pop()
            dfs(cur+1)
        dfs(0)
        # count(s)
        return res




S = "ABC"
print(Solution().uniqueLetterString(S))
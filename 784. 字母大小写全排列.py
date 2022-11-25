from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def swap(word):
            if word.isupper():
                return word.lower()
            else:
                return word.upper()

        def dfs(list_s,pos):
            while pos < len(list_s) and list_s[pos].isdigit():
                pos+=1
            if pos == len(list_s):
                res.append("".join(list_s))
                return
            dfs(list_s,pos+1)
            list_s[pos] = swap(list_s[pos])
            dfs(list_s,pos+1)
            list_s[pos] = swap(list_s[pos])
        dfs(list(s),0)
        return res

s = "a1b2"
print(Solution().letterCasePermutation(s))
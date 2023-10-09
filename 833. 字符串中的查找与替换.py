from typing import List
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        if not indices:
            return s
        res = ""
        i = 0
        while i < len(s):
            if i in indices:
                index = indices.index(i) # 找到索引
                source = sources[index]
                target = targets[index]
                if s[i:i+len(source)] == source:
                    res += target
                    i += len(source)
                else:
                    res += s[i]
                    i += 1
            else:
                res += s[i]
                i += 1
        return res

s = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]

s = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(Solution().findReplaceString(s, indexes, sources, targets))
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        record = [0]*26
        res = []
        for i,w in enumerate(s):
            record[ord(w) - 97] = i
        t = s[0]
        r = record[ord(t) - 97]
        last = 0
        for i,w in enumerate(s):
            if i == r and t == w:
                res.append(i-last+1)
                print(i,last)
                last = i+1
                continue
            if record[ord(w) - 97]>r:
                r = record[ord(w) - 97]
                t = w
        return res


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
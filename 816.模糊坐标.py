from itertools import product
from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:len(s)-1]
        res = []
        # print(s)
        def generate(s_):
            if len(s_) == 0 or int(s_) == 0 and len(s_)>1 :
                return []
            if s_[0] == "0" and len(s_) == 1:
                return ["0"]
            if len(s_) >1 and int(s_[1:]) == 0:
                return [s_]
            g_s = []
            if s_[0] == "0":
                for i in range(len(s_)-1,0,-1):
                    if s_[i] == "0":
                        return []
                    else:
                        break
                return ["0."+s_[1:]]
            else:
                for i in range(1,len(s_)):
                    for j in range(len(s_) - 1, i, -1):
                        if s_[j] == "0":
                            return [s_]
                        else:
                            break
                    t = s_[:i]+"."+s_[i:]
                    g_s.append(t)
            return g_s+[s_]
            #插入小数点

        for l in range(1,len(s)):
            print(s[:l],s[l:])
            left = generate(s[:l])
            print(left)
            right = generate(s[l:])
            print(right)
            if len(left)!=0 and len(right)!=0:
                for z in product(left,right):
                    res.append("("+z[0]+", "+z[1]+")")
        return res
s = "(0123)"
s = "(100)"
# s = "(123)"
# s = "(00011)"
# s = "(0010)"
# s = "(0110)"
print(Solution().ambiguousCoordinates(s))
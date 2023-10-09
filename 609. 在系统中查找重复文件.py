from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            path = path.split()
            for i in range(1,len(path)):
                temp = path[i].split("(")
                d[temp[1][:-1]].append(path[0]+"/"+temp[0])
        res = []
        for temp in d.values():
            if len(temp) >1:
                res.append(temp)
        return res

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]

print(Solution().findDuplicate(paths))
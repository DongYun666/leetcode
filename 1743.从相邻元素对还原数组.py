from collections import defaultdict
from typing import List

class Solution:
    def restoreArray1(self, adjacentPairs: List[List[int]]) -> List[int]:
        left,right = [adjacentPairs[0][0]],[adjacentPairs[0][1]]
        record = [left[0],right[0]]

        cnts = defaultdict(list)
        for x,y in adjacentPairs:
            cnts[x].append(y)
            cnts[y].append(x)
        print(cnts)

        #对于左边
        q_left = []
        q_left.append(left[0])
        while q_left:
            temp = q_left.pop()
            for x in cnts[temp]:
                if x not in record:
                    left.append(x)
                    q_left.append(x)
                    record.append(x)
        q_right = []
        q_right.append(right[0])
        while q_right:
            temp = q_right.pop()
            for x in cnts[temp]:
                if x not in record:
                    right.append(x)
                    q_right.append(x)
                    record.append(x)
        left.reverse()
        return left+right

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ad_congut = defaultdict(int)
        cnts = defaultdict(list)
        for x,y in adjacentPairs:
            ad_congut[x]+=1
            ad_congut[y]+=1
            cnts[x].append(y)
            cnts[y].append(x)

        start = -1
        for x,count in ad_congut.items():
            if count == 1:
                start = x
                break
        n = len(adjacentPairs)+1
        res = [0]*(n)
        res[0] = start
        res[1] = cnts[start][0]
        for i in range(1,n):
            x = res[i-1]
            for j in cnts[x]:
                if j != res[i-2]:
                    res[i]=j
        return res
adjacentPairs = [[4,-2],[1,4],[-3,1]]
adjacentPairs = [[2,1],[3,4],[3,2]]
print(Solution().restoreArray(adjacentPairs))
from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1,len(travel)):
            travel[i]+=travel[i-1]
        P,M,G = 0,0,0
        P_i,M_i,G_i = 0,0,0
        for i,g in enumerate(garbage):
            P_c,M_c,G_c=g.count('P'),g.count('M'),g.count('G')
            if P_c!=0:
                P+=P_c
                P_i = i
            if M_c!=0:
                M+=M_c
                M_i = i
            if G_c!=0:
                G+=G_c
                G_i = i
        res = P+M+G
        if P_i!=0:
            res+=travel[P_i-1]
        if M_i!=0:
            res+=travel[M_i-1]
        if G_i!=0:
            res+=travel[G_i-1]
        return res








garbage = ["MMM", "PGM", "GP"]
travel = [3, 10]
print(Solution().garbageCollection(garbage, travel))
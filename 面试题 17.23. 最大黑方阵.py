from collections import defaultdict
from typing import List
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        rMatrix = defaultdict(int)
        cMatrix = defaultdict(int)
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j] == 0:
                    rMatrix[i,j] = rMatrix[i, j + 1] + 1
                    cMatrix[i,j] = cMatrix[i + 1, j] + 1
                else:
                    rMatrix[i,j] = 0
                    cMatrix[i,j] = 0
        res = [0,0,0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    lenght = min(rMatrix[i,j],cMatrix[i,j])
                    curlen = res[2]
                    while lenght>=curlen:
                        if cMatrix[i,j+lenght-1] >= lenght and rMatrix[i+lenght-1,j] >=lenght:
                            if lenght == curlen:
                                res = min(res,[i,j,lenght],key=lambda x:(x[0],x[1]))
                            res = max(res,[i,j,lenght],key=lambda x:x[2])
                        lenght-=1
        return res if res != [0,0,0] else []
        # print(matrix,rMatrix,cMatrix)




# matrix = [
#    [0,1,1],
#    [1,0,1],
#    [1,1,0]
# ]
matrix = [[1]]
print(Solution().findSquare(matrix))
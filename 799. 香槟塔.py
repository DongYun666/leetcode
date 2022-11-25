class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(1,query_row+1):
            next_row = [0]*(i+1)
            for j,value in enumerate(row):
                if value > 1:
                    next_row[j] += (value-1)/2
                    next_row[j+1] += (value-1)/2
            row = next_row
        return min(1,row[query_glass])

poured = 2
query_glass = 1
query_row = 1

print(Solution().champagneTower(poured,query_row,query_glass))
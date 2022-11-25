from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr_xor_sum = [arr[0]]
        res = []
        for i in range(1,len(arr)):
            arr_xor_sum.append(arr_xor_sum[-1]^arr[i])
        # print(arr_xor_sum)
        for L,R in queries:
            if L == 0:
                res.append(arr_xor_sum[R])
            else:
                res.append(arr_xor_sum[R]^arr_xor_sum[L-1])
        return res



arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
print(Solution().xorQueries(arr, queries))
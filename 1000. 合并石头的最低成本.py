from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        length = [cuts[0]]
        for i in range(1,len(cuts)):
            length.append(cuts[i] - cuts[i-1])
        length.append(n - cuts[-1])
        print(length)
        res = 0
        while len(length) > 1:
            # 找到连续和最小的两个
            min_sum = float('inf')
            min_index = 0
            for i in range(len(length)-1):
                if length[i] + length[i+1] < min_sum:
                    min_sum = length[i] + length[i+1]
                    min_index = i
            res += min_sum
            length[min_index] = min_sum
            length.pop(min_index+1)
            print(length)
        return res
    
n = 7
cuts = [1,3,4,5]

n = 36
cuts = [13,17,15,18,3,22,27,6,35,7,11,28,26,20,4,5,21,10,8]
print(Solution().minCost(n,cuts))
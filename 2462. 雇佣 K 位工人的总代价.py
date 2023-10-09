import heapq
from typing import List
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res,n = 0,len(costs)
        if 2 * candidates < n:
            pre = costs[:candidates]
            heapq.heapify(pre)
            suff = costs[-candidates:]
            heapq.heapify(suff)
            i,j = candidates,n-candidates-1
            while i <= j:
                #先从两个最小堆中挑选最小的一个出来
                if k <= 0:
                    break
                if pre[0] <= suff[0]:
                    res += pre[0]
                    k -= 1
                    heapq.heappop(pre)
                    heapq.heappush(pre,costs[i])
                    i += 1
                else:
                    res += suff[0]
                    k -= 1
                    heapq.heappop(suff)
                    heapq.heappush(suff,costs[j])
                    j -= 1
                
            costs = pre + suff
        costs.sort()
        res += sum(costs[:k])
        return res
costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
k = 11
candidates = 2

costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4
print(Solution().totalCost(costs,k,candidates))
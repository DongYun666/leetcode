from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            remain = gas[i] - cost[i]
            cnt = 0
            while cnt < n:
                if remain < 0:
                    break
                remain += gas[(i + cnt + 1) % n] - cost[(i + cnt + 1) % n]
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))
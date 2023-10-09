from typing import List
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        if sum(vat) == 0:
            return 0
        ans = float('inf')
        for i in range(1,10001):
            tmp = 0
            for j in range(n):
                if vat[j] == 0:
                    continue
                tmp = max(tmp,vat[j] // (bucket[j] + i) + vat[j] % (bucket[j] + i))
            ans = min(ans,tmp + i)
        return ans
bucket = [9,0,1]
vat = [0,2,2]

bucket = [1,3]
vat = [6,8]
print(Solution().storeWater(bucket,vat))
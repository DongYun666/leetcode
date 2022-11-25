from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i,n = 0,len(data)
        while i<n:
            t = data[i]
            j = 7
            while j >= 0 and (t>>j)&1 == 1:j-=1
            cnt = 7-j
            if cnt == 1 or cnt>4:return False
            if i+cnt-1>n:return False
            for k in range(i+1,i+cnt):
                if (data[k]>>7)&1 == 1 and (data[k]>>6)&1 == 0:continue
                return False
            if cnt == 0:i+=1
            else:i+=cnt
        return True


data = [197, 130, 1]
data = [235,140,4]
print(Solution().validUtf8(data))
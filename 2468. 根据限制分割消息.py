from typing import List
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        f = [0] * (n + 1)
        for i in range(1,n + 1):
            j = i
            while j:
                f[i] += 1
                j //= 10
        print(f)

        def genearate(start,length,which,all):
            return message[start:start+length] + "<" + str(which) + "/" + str(all) + ">"

        for x in range(1,n+1):
            total = 0
            i,j = 1,10
            while i < x:
                each = limit - 3 - f[x] - f[i]
                total += each * (min(j,x) - i)
                i *= 10
                j *= 10
            if n - total > 0 and n - total <= limit - 3 - f[x] * 2:
                res = []
                start = 0
                for i in range(1,x):
                    each = limit - 3 - f[x] - f[i]
                    res.append(genearate(start,each,i,x))
                    start += each
                res.append(genearate(start,n - start,x,x))
                return res
        return []
    def splitMessage1(self, message: str, limit: int) -> List[str]:
        n = len(message)
        f = [0] * (n + 1)
        for i in range(1,n + 1):
            j = i
            while j:
                f[i] += 1
                j //= 10

        def genearate(start,length,which,all):
            return message[start:start+length] + "<" + str(which) + "/" + str(all) + ">"
        
        def check(mid):
            total = 0
            i,j = 1,10
            while i < mid:
                each = limit - 3 - f[mid] - f[i]
                total += each * (min(j,mid) - i)
                i *= 10
                j *= 10
            return total >= n
        
            # return 0 < n - total <= limit - 3 - f[mid] * 2
        
        left,right = 1,n
        while left < right:
            mid = (left + right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        # 此时的mid 代表划分的总数
        # print(mid,left,right)
        x = left - 1
        res = []
        start = 0
        for i in range(1,x):
            each = limit - 3 - f[x] - f[i]
            res.append(genearate(start,each,i,x))
            start += each
        res.append(genearate(start,n - start,x,x))
        return res


    
message = "this is really a very awesome message"
limit = 9

# message = "short message"
# limit = 15

print(Solution().splitMessage1(message,limit))
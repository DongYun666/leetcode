from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        flag = True
        index = 0
        temp = k
        if k == 1:
            return [i for i in range(1,n+1)]
        while k != 0:
            if flag:
                res.append(res[index]+k)
            else:
                res.append(res[index]-k)
            k-=1
            index+=1
            flag = not flag
        return res+[i for i in range(temp+2,n+1)]


n = 7
k = 3
print(Solution().constructArray(n,k))
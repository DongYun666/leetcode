class Solution:
    def Regular_sequence(self,n,num):
        num.sort()
        res = 0
        for i in range(1,n+1):
            res+=abs(num[i-1]-i)
        return res

n = int(input())
num = list(map(int,input().split()))
print(Solution().Regular_sequence(n,num))

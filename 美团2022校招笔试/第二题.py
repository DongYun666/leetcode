class Solution:
    def Function(self,n,num):
        res = []
        for i in range(len(num)):
            res.append(self.mex(num[0:i]+num[i+1:]))
        return res
    def mex(self,num):
        num.sort()
        if num[-1] == len(num)-1:
            return num[-1]+1
        for i in range(max(num)):
            if i != num[i]:
                return i
n = int(input())
num = list(map(int,input().split()))
for r in Solution().Function(n,num):
    print(r,end=" ")

# 4
# 5 0 3 1
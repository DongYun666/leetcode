class Solution:
    def Function(self,n,m,k,a,b,c):
        def dfs(k,a,b,c,index):
            if index >= len(c):
                return 0
            if k == c[index]:
                return a[index]+dfs(k,a,b,c,index+1)
            else:
                return max(dfs(k,a,b,c,index+1),b[index]+dfs(c[index],a,b,c,index+1))
        return dfs(k,a,b,c,0)



n,m,k = list(map(int,input().split()))
c = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(Solution().Function(n,m,k,a,b,c))

# 3 5 1
# 2 1 2 3 2
# 9 6 2 1 7
# 1 3 0 5 2
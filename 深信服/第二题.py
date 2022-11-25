n,m = list(map(int,input().split()))
dict = []
for i in range(n):
    dict.append(list(map(int,input().split())))
dp = [[0 for _ in range(m)] for i in range(n)]
def uniquepaths(n,m):
    for i in range(m):
        if dict[0][i]!=1:
            dp[0][i] =1
        else:
            break
    for i in range(n):
        if dict[i][0] != 1:
            dp[i][0] = 1
        else:
            break
    for i in range(1,n):
        for j in range(1,m):
            if dict[i][j]!=1:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[n-1][m-1]
print(uniquepaths(n,m))

# 5 5
# 0 1 0 0 0
# 0 1 0 0 0
# 0 1 0 0 0
# 0 1 0 0 0
# 0 0 0 0 0
# 1

num = list(map(int,input().split()))
def func(num):
    if len(num) == 1:
        return num[0]
    dp = [0 for _ in range(len(num)+2)]
    for i in range(2,len(dp)):
        dp[i] = max(dp[i-1],dp[i-2]+num[i-2])
    return dp[len(num)+1]
print(func(num))


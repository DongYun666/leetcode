src = input()
target = input()
def f(src,target):
    n = len(src)
    m = len(target)
    if n * m == 0:
        return n + m
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            l = dp[i - 1][j] + 1
            d = dp[i][j - 1] + 1
            l_d = dp[i - 1][j - 1]
            if src[i - 1] != target[j - 1]:
                l_d += 1
            dp[i][j] = min(l, d, l_d)
    return dp[n][m]
print(f(src,target))
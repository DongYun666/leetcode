n = int(input())
d = []
ans = 0
for i in range(n):
    temp = list(map(int,input().split()))
    d.append(temp)
for i in range(n):
    for j in range(n):
        ans += abs(d[i][j]-d[j][i])
print(ans)
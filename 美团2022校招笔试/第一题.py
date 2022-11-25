a,b  = list(map(int,input().split()))
ans = 0
if b <=9:
    ans = 11-a
else:
    ans = b+2-a
print(ans)



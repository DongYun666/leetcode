def Reverse_pairs_count(num):
    for i in range(len(num)):
        if num[i] == 0:
            continue
        else:
            return num[i:].count(0)
    return 0

n,m = list(map(int,input().split()))
num = list(map(int,input().split()))
res = Reverse_pairs_count(num)
for i in range(len(num)-m):
    temp = num
    for j in num[i:i+m]:
        if num[j] == 0:
            num[j] = 1
        else:
            num[j] = 0
    res = min(res,Reverse_pairs_count(num))
    num = temp
print(res)

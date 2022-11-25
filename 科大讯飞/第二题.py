N = int(input())
num = list(map(int,input().split()))
L,R = list(map(int,input().split()))
def func(num):
    if sum(num)<L*N or sum(num)>R*N:
        return -1
    temp_L = 0
    temp_R = 0
    for n in num:
        if n < L:
            temp_L += L-n
        elif n > R:
            temp_R += n-R
    return max(temp_R,temp_L)
print(func(num))


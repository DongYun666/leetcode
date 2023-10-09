import math

mod = 10**9 + 7
def sumFirstK(k):
    m = int(math.sqrt(k * 2 - 1))
    res = 0
    for i in range(1,m +1):
        res += i*(i+1)//2 % mod
    temp = k - m * (m + 1)//2
    m += 1
    while temp > 0:
        res += m
        m -= 1
        temp -= 1
    return res
    
n = int(input())
print(sumFirstK(n))
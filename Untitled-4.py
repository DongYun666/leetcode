
import math

def check(num):
    if num % math.sqrt(num):
        return False
    return True

def solution(nums,l,r,x):
    for i in range(l,r+1):
        if not check(nums[i] * x):
            return nums[i]
    return -1

n,q = list(map(int,input().split()))
nums = list(map(int,input().split()))
res = []
for i in range(q):
    l,r,x = list(map(int,input().split()))
    res.append(solution(nums,l-1,r-1,x))
for r in res:
    print(r)

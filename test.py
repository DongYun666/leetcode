# count = [1993,2171,47,114,1503,2749,3569,6749,2287,25]
# sum_c = sum(count)
# socre = [0.99924680,0.99953917,0.90697674,0.89908257,0.99074074,0.99836512,0.99915896,0.99955569,0.99978133,0.93617021]
# res = 0
# print(sum(socre)/10)
# for i in range(10):
#     res += (1 - count[i]/sum_c)*socre[i]
# print(res)           
# # print(sum(count))

# fruits = ['apple', 'banana', 'orange']

# for fruit in fruits:
#     if fruit == 'banana':
#         print("Skipping banana")
#         continue
#     print(fruit)

# else:
#     print("Loop completed")


# s = "A"
# print(ord(s))
# print(chr(65))

# test = [4,5]
# nums = [-1,4,3,1]
# nums[nums[1]-1],nums[1] = nums[1],nums[nums[1]-1]
# print(nums)

import bisect
from collections import Counter, defaultdict
import heapq


# l1 = [1,1,2,2,3,4]
# print(list(Counter(l1).keys()))
# nums = [1,2,3,4,5,6,7,8,9]
# for a, b in zip(nums, nums[1:]):
    # print(a,b)
# 设置 defaultdict 的默认值为 0)
# dect = defaultdict(lambda:-1)
# dect[3] = 4
# print(dect[3])
# print(dect[4])
# nums = [4,7,2,1,5,3,6,8]]
# print(set(nums))
# print(nums.pop())
# max_t = 2
# st = 0
# max_t = max_t + 1 if st else 0
# print(max_t)

def maxLength(nums, target):
    n = len(nums)
    preSum = [0] * (n + 1)
    for i in range(1, n):
        preSum[i] = preSum[i-1] + (nums[i] - nums[i-1] - 1)
    preSum[n] = preSum[n-1]
    res = 1
    start = 0
    for end in range(1, n + 1):
        while preSum[end] - preSum[start] > target:
            start += 1
        res = max(res, end - start)
    return res

# nums = [1,5,6,7,9,10]
# target = 3
# print(maxLength(nums,target))

# s = "abcdefg"
# s[0] = "A"
# print(s)
# num = 5
# print(num.bit_length())
# arr = [3,2,1]
# k = 2
# arr = heapq.nsmallest(k, arr)
# print(arr)

# s = "   ab  cd  "
# print(s.strip())

def last_remaining(n, m):
    if n == 1:
        return 0
    
    f = 0
    for i in range(2, n + 1):
        f = (f + m) % i
        print(f)
    
    return f

# 示例用法
# n = 5
# m = 3
# result = last_remaining(n, m)
# print("剩下的最后一个数字是:", result)

# nums = [1,9,2,8,7,6,3,4,5]
# nums = heapq.heapify(nums)
# k = 3
# for i,num in enumerate(nums[k:],k):
    # print(i,num)

# n = 6
# bit = 0
# while (n - 1) >> bit:
    # bit += 1
# print(bit)
# n = 7
# parent = [-1,0,0,1,1,2,2]
# m = n.bit_length() - 1
# pa = [[p] + [-1] * m for p in parent]
# for i in range(m):
#     for x in range(n):
#         p = pa[x][i]
#         if p != -1:
#             pa[x][i+1] = pa[p][i]
# print(pa)
# x = [i + 1 for i in range(10)]
# print(x)
# print(bisect.bisect_left(x, 5))
# print(bisect.bisect_right(x, 5))
# nums = [1,2,2,2,3,4,5,6,7,8,9]
# l,r = 0,len(nums)
# target = 9
# while l < r:
#     mid = (l+r)//2
#     if nums[mid] > target:
#         r = mid
#     else:
#         l = mid + 1
# print(l)


# class Solution:
#     def sum(self, num1: int, num2: int) -> int:
#         num1 &= 0xffffffff
#         num2 &= 0xffffffff
#         while num2 != 0:
#             num1, num2 = num1 ^ num2, (num1 & num2) << 1 & 0xffffffff
#         print(num1)
#         print(0x80000000)
#         print(0xffffffff)
#         return num1 if num1 < 0x80000000 else ~(num1 ^ 0xffffffff)


# num1 = -1
# num2 = -2
# print(Solution().sum(num1, num2))        
# s = "abc"
# print([c for i,c in enumerate(s) if i % 2 == 0])\

# tasks = [[1,3,2],[2,5,3],[5,6,2]]
# tasks.sort(key=lambda x:x[1],reverse=True)
# print(tasks)
# for i in range(1,10000,10):
    # print(i)
# x = 5
# print(x // 2)

# def backtrack(nums,target, i, subset):
#     if sum(subset) == target:
#         return True
    
#     if i >= len(nums):
#         return False

#     # 选择当前元素
#     subset.append(nums[i])
#     if backtrack(nums,target, i, subset):
#         return True
#     subset.pop()

#     # 不选择当前元素
#     return backtrack(nums,target, i+1, subset)

# def findZeroSum(nums,target):
#     return backtrack(nums,target, 0, [])

# nums = [-1,1]
# print(findZeroSum(nums,100)) # True

s = "abcd"

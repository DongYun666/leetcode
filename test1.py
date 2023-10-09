# # -*- codeing = utf-8 -*-
# # @Time : 2021/11/22 15:13
# # @Author : DongYun
# # @File : test1.py
# # @Software : PyCharm
# # class Solution:
# #     def multi(self,x,y):
# #         a,b, res,i  = abs(x),abs(y),0,0
# from math import gcd






# # def printAllFolds(N):
# #     def printProcess(i, N, isDown):
# #         if i > N:
# #             return
# #         printProcess(i+1, N, True)
# #         print("Down" if isDown else "Up", end=' ')
# #         printProcess(i+1, N, False)
# #     printProcess(1, N, True)
# # # print(printAllFolds(1))
# # def process(M, N, a, b, k):
# #     if a < 0 or a > M or b < 0 or b > N:
# #         return 0
# #     if k == 0:
# #         return 1
# #     return process(M, N, a - 1, b, k-1) \
# #            + process(M, N, a, b - 1, k-1) \
# #            + process(M, N, a + 1, b, k-1)\
# #            + process(M, N, a, b + 1, k-1)
# # x = process(4, 4, 1, 1, 4)
# # g = gcd(4 ** 4, x)
# # print( str(int(x/ g)) + '\/' + str(int(4**4 / g)))
#
# ways = 0
# def process(arr, index, rest):
#      if index == len(arr):
#          return 1 if rest == 0 else 0
#      zhang = 0
#      while arr[index] * zhang < rest:
#         global ways
#         ways += process(arr, index+1, rest - arr[index]*zhang)
#         zhang += 1
#      return ways
# # print(process([3,5,10,2],0,5))
#
#
# from treelib import Tree, Node
# tree = Tree()
# tree.create_node(tag='Node-5', identifier='node-5', data=5)
# tree.create_node(tag='Node-10', identifier='node-10', parent='node-5', data=10)
# tree.create_node('Node-15', 'node-15', 'node-10', 15)
# tree.show()
#
# node = Node(data=50)
# tree.add_node(node, parent='node-5')
# node_a = Node(tag='Node-A', identifier='node-A', data='A')
# tree.add_node(node_a, parent='node-5')
# tree.show()
#
# print(tree.identifier)
#
#
# temp = []
# temp.append(1)
# temp.append(2)
# temp.append(3)
# temp.append(4)
# temp.append(5)
# print(temp)
# temp.pop()
# print(temp)
#
#
# print(1//10)
# def count_len(n):
#     l = 1
#     while True:
#         if (10 ** l - 1) % n == 0:
#             break
#         l += 1
#     return l
# n = 6
# print(count_len(n))
# for i in range(1,111):
#     print(i/111)
# print('abcd'>'dcba')
# print(reversed([1,2,3,4]))
# res = [[1,2],[3,4],[5,6]]
# for i in map(sum,res):
#     print(i)
# a = [3,8,1,2,0,9,4,5,7,6]
# print(sorted(enumerate(a),key=lambda x:x[1]))
# a = {1,2,3,4,5,6}
# print({7} | a)
# def permute(nums):
#     n = len(nums)
#     dp = [[[nums[0]]]] + [[] for _ in range(n - 1)]
#     print(dp)
#     for i in range(1, n):
#         for pmt in dp[i-1]:
#             for j in range(i + 1):
#                 dp[i].append(pmt[:j] + [nums[i]] + pmt[j:])
#     return dp[n-1]
# print(permute([0,1,2,3]))



n = 15
a = []
while n:
            lb = n & -n
            a.append(lb)
            n ^= lb
print(a)
print(bin(14))
print(bin(-14))
print(bin(14 & -14))

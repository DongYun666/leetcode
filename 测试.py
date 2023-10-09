# x = [1,2,34,5]
# print(x.reverse())
# fir = int(input())
# fir_list = list(map(int,input().split()))
# sec = int(input())
# sec_list = list(map(int,input().split()))
# print("".join(str(x) for x in sorted(list(set(fir_list+sec_list)))))
# print("".join(list(set(fir_list+sec_list))))
# from collections import Counter
#
# target = Counter(input())
# source = Counter(input())
#
# from tkinter import *
# from tkinter import messagebox
# def F1():
#     if(v1.get()==1):
#         if(v2.get()==1):
#             text2.insert("insert","5角")
#             text1.insert("insert","可乐")
#         elif(v2.get()==2):
#             text2.insert("insert","5角")
#             text1.insert("insert","雪碧")
#         elif (v2.get() == 3):
#             text2.insert("insert", "5角")
#             text1.insert("insert", "红茶")
#
#         else:
#             messagebox.showinfo("提示","请选择饮料")
#     elif(v1.get()==2):
#         if(v2.get()==1):
#             text2.insert("insert","不找零")
#             text1.insert("insert","可乐")
#         elif(v2.get()==2):
#             text2.insert("insert","不找零")
#             text1.insert("insert","雪碧")
#         elif (v2.get() == 3):
#             text2.insert("insert", "5角")
#             text1.insert("insert", "红茶")
#         else:
#             messagebox.showinfo("提示","请选择饮料")
#     else:
#         messagebox.showinfo("提示","请投币！")
# def root_update():
#     v1.set(3)
#     v2.set(3)
#     text1.delete('1.0', END)
#     text2.delete('1.0', END)
#
# #建立窗口root
# root=Tk()
# #窗口标题
# root.title("自动售卖机")
# #窗口背景
# root.configure(background="#F8F8FF")
# #设置窗口大小且不可变
# root.geometry('400x400')
# root.resizable(0,0)
# #设置关联变量
# v1=IntVar()
# v2=IntVar()
#
# #选择标签用于恢复选择按钮
# Label1=Radiobutton(root,text='请投币:',bg='red',width="10",height="2",variable=v1,value=3)
# Label1.pack()
# Label1.place(x=0,y=0)
# Label2=Radiobutton(root,text='选择饮料:',bg='red',width="10",height="2",variable=v2,value=3)
# Label2.pack()
# Label2.place(x=0,y=110)
# Label3=Label(root,text='请取饮料:',bg='red',width="10",height="2")
# Label3.pack()
# Label3.place(x=0,y=300)
# Label4=Label(root,text='找零:',bg='red',width="10",height="2")
# Label4.pack()
# Label4.place(x=200,y=300)
# #花钱选择
# r1=Radiobutton(root,text='2元',variable=v1,value=1)
# r1.pack()
# r1.place(x=100,y=50)
# r2=Radiobutton(root,text='1.5元',variable=v1,value=2)
# r2.pack()
# r2.place(x=200,y=50)
# #饮料选择
# r3=Radiobutton(root,text='可乐',variable=v2,value=1)
# r3.pack()
# r3.place(x=100,y=150)
# r4=Radiobutton(root,text='雪碧',variable=v2,value=2)
# r4.pack()
# r4.place(x=200,y=150)
# r5=Radiobutton(root,text='红茶',variable=v2,value=3)
# r5.pack()
# r5.place(x=300,y=150)
# #进行操作按钮
# button1=Button(root,text='确认',width='5',height='2',command=F1)
# button1.place(x=100,y=200)
# button2=Button(root,text='复位',width='5',height='2',command=root_update)
# button2.place(x=200,y=200)
# text1 = Text(root,width=6,height='3')
# text1.pack()
# text1.place(x=100, y=300)
# text2 = Text(root,width=6,height='3')
# text2.pack()
# text2.place(x=300, y=300)
# root.mainloop()
import bisect
import math
from collections import Counter, deque, defaultdict
from itertools import product
from typing import List


# s = "12345"
# print(s.find("1"))
#
# temp = [1,2,3,4,5]
# print(sum(temp))

# s = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
# print(s.count("AAAAA"))

#
# num = list(map(int,input().split()))
# print("%.2f" % (num[1]/(num[2]*0.01)))
# res = []
# for i in range(1,301):
#     for j in range(1,301):
#         for k in range(1,301):
#             if i+33*j+int(582/k) == 2982:
#                 res.append([i,j,k])
# n = [1,2,3]
# print(n.pop(0))
# print(n)
# n = [1,2,3]
# n+=1
# print(n)
# S = "211.101.245.171,211.101.245.182,211.101.245.184,8.143.2.128,125.65.42.44,125.65.42.147,125.65.42.252,60.205.142.209,221.179.238.101,118.195.145.15,119.45.93.91,119.45.171.76,119.45.168.250,118.195.160.188,119.45.20.160,118.195.151.129,40.77.167.70,161.8.159.125,157.55.39.120,125.67.17.213,207.46.13.140,157.55.39.163,157.55.39.164,119.52.246.63,175.27.248.150,119.45.93.208,139.204.172.97,119.45.171.198,40.77.167.75,182.16.17.234,43.129.158.31"
# list_S = S.split(",")
# for i in list_S:
#     print(i)
# print(len(list_S))
# print(ord("e"))
# print(min(1,2,3))

# n = int(input())
# num = []
# for _ in range(n):
#     temp = list(map(int,input().split()))
#     num.append(temp)
# num = list(map(list, zip(*num)))[::-1]
# for i in range(n):
#     for j in range(n):
#         print(num[i][j],end=' ')
#     print()
# print("12234" in "12234355667")
# x = "1234567"
# y = list(x)
# y.reverse()
# print(x,y)
# nums = [1,2,3,4,5]
# print(bisect.bisect(nums,7))
# print(max([[1,2],[3,4]]))t
# test = "123456789"
# print(test.count('0'))

# T = int(input())
# res = []
# for _ in range(T):
#     Weights = list(map(int,input().split()))
#     words = input()
#     ans = 0
#     temp = []
#     for i in range(len(words)):
#         temp.append(Weights[ord(words[i])-97])
#         if temp[-1]>1:
#             ans +=1
#     res.append(ans if ans > 0 else 1 )
#
# for r in res:
#     print(r)
# print("1">"0")

# n = 123
# n = list(str(n)).reverse()
# print(n)

# num = [0,1,2,4,5]

#
# def bisearch(arr, x):
#     if x<arr[0]:
#         return -1
#     if x > arr[-1]:
#         return len(arr)
#     left, right = -1, len(arr)-1
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] == x:
#             return mid
#         if arr[mid] > x:
#             right = mid
#         else:
#             left = mid+1
#     return left
# num = [1,3,4,7]
# print(bisearch(num, 0))

#
# print(bisearch(num,5))
# num1 = [1,1,1,1]
# num2 = [2,2,2,2]
# num = [1, 1, 2, 2, 2, 3]
# cnt = Counter(num)
# temp = cnt.keys()
# print(1 in temp)
# stock = {}
# stock[1] = 1
# stock[3] = 3
# stock[2] = 2
#
# temp = list(stock.keys())
# print(temp)
# print(stock.get(temp[-1]))

class StockPrice:

    def __init__(self):
        self.stock = {}
        self.max_ = 0
        self.min_ = 0

    def update(self, timestamp: int, price: int) -> None:
        self.stock[timestamp] = price
        self.max_ = max(self.max_, price)
        self.min_ = min(self.min_, price)

    def current(self) -> int:
        temp = list(self.stock.keys())
        return self.stock.get(temp[-1])

    def maximum(self) -> int:
        return self.max_

    def minimum(self) -> int:
        return self.min_

# SP = StockPrice()
# SP.update(1,10)
# SP.update(2,5)
# print(SP.current())
# print(SP.maximum())
# SP.update(1,3)
# print(SP.maximum())
# SP.update(4,2)
# print(SP.minimum())

#
#
# stock = {}
# stock[0] = 0
# stock[1] = 1
# stock[2] = 2
# stock[3] = 3
# print(max(stock.values()))

# q = deque()
# for i in range(5):
#     q.append(i)
# print(q.popleft())
# print(q.pop())

# s = "abcd"
# print(sorted(s))
# stack = [1,2,3,4]
# print(stack.pop())
#
# from typing import List
# def f(nums: List[int]):
#     res = [0]*len(nums)
#     stack = []
#     for i,num in enumerate(nums):
#         while len(stack)>0 and stack[-1][1]<num:
#             res[stack[-1][0]] = num
#             stack.pop()
#         stack.append((i,num))
#     return res
#
#
# head = [2,7,4,3,5]
# head = [2,1,5]
# print(f(head))

def generate(s):
    if len(s) == 0:
        return []
    g_s = []
    if s[0] == "0" and len(s) == 1:
        return ["0"]
    if s[0] == "0":
        return ["0."+s[1:]]
    else:
        for i in range(1,len(s)):
            t = s[:i]+"."+s[i:]
            g_s.append(t)
    return g_s
# print(generate(""))
# x = [1,2,3]
# y = [4,5,6]
# for z in product(x,y):
#     print(z)

def generate(s_):
    if len(s_) == 0 or int(s_) == 0 and len(s_) > 1:
        return []
    if s_[0] == "0" and len(s_) == 1:
        return ["0"]
    if len(s_) > 1 and int(s_[1:]) == 0:
        return [s_]
    g_s = []
    if s_[0] == "0":
        for i in range(len(s_) - 1, 0, -1):
            if s_[i] == "0":
                return []
            else:
                break
        return ["0." + s_[1:]]
    else:
        for i in range(1, len(s_)):
            for j in range(len(s_) - 1, i, -1):
                if s_[j] == "0":
                    return [s_]
                else:
                    break
            t = s_[:i] + "." + s_[i:]
            g_s.append(t)
    return g_s + [s_]
# print(generate("110"))
#

# print(set("231d"))
# print(set("31a2"))
# print(set("231d") > set("31a2"))

# print(1.0%1 == 0)

# x = [[1,7,3],
#      [4,6,5]]
# x = [1,2,3,4,5,6]
# print(max())
# print(math.sqrt(4) == 2)

# def count(s_):
#     ans = 0
#     for i in range(len(s_)):
#         ans += int(s_[i]) * 2 ** i
#     return ans
# print(count("1001"))


# def count(s_):
#     ans = 0
#     for i in range(len(s_) - 1, -1, -1):
#         ans += int(s_[i]) * 2 ** (len(s_)-i-1)
#     return ans
# print(count("0000101"))

# def massage(nums):
#     n = len(nums)
#     if n == 0:
#         return 0
#     dp0,dp1 = 0,nums[0]
#     for i in range(1,n):
#         t0 = max(dp0,dp1)
#         t1 = dp0+nums[i]
#         dp0,dp1 = t0,t1
#     return max(dp0,dp1)
#
# nums = [2,1,4,5,3,1,1,3]

# print(massage(nums))
# print(1<<0)
# s = "1010110110000"
# print(s)
# print(bisect.bisect_right(s,"11"))

# data = [[1,0,0,1],[0,1,1,0]]
# print(sum(sum(t)for t in data))
# from typing import List
# class Solution:
#     def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
#         def get_next(s):
#             return [int(i > 0 and i < 7 and s[i-1] == s[i+1]) for i in range(8)]
#         used = {}
#         while n > 0:
#             c = tuple(cells)
#             if c in used:
#                 n %= (used[c]-n)
#             used[c] = n
#             if n > 0:
#                 n -=1
#                 cells = get_next(cells)
#         return cells
#
# cells = [0,1,0,1,1,0,0,1]
# n = 7
# print(Solution().prisonAfterNDays(cells,n))
#
#
# nums = [20,46,15,39]
# nums1 = sorted(nums)
# d = defaultdict(int)
# for i in range(len(nums1)):
#     d[nums1[i]] = i
# flag = [False] * len(nums)
# res = 0
# for i in range(len(nums)):
#     if not flag[i]:
#         j = i
#         while not flag[j]:
#             flag[j] = True
#             j = d[nums[j]]
#         res += 1
# print(len(nums)-res)

# nums = [1,2,3,4,5]
# print("".join(nums))

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1, 0]] * n for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        def update(x, y, u, v):
            if u >= n or v >= n or dp[u][v][0] == -1:
                return
            if dp[u][v][0] > dp[x][y][0]:
                dp[x][y] = dp[u][v][:]
            elif dp[u][v][0] == dp[x][y][0]:
                dp[x][y][1] += dp[u][v][1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not (i == n - 1 and j == n - 1) and board[i][j] != "X":
                    update(i, j, i + 1, j)
                    update(i, j, i, j + 1)
                    update(i, j, i + 1, j + 1)
                    if dp[i][j][0] != -1:
                        dp[i][j][0] += (0 if board[i][j] == "E" else ord(board[i][j]) - 48)
        print(dp)
        return [dp[0][0][0], dp[0][0][1] % (10**9 + 7)] if dp[0][0][0] != -1 else [0, 0]

# board = ["E12",
#          "1X1",
#          "21S"]
# print(Solution().pathsWithMaxScore(board))

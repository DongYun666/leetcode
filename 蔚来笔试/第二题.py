t = int(input())
# res = []
num = []
max_num = float("-inf")
for i in range(t):
    n = int(input())
    num.append(n)
    max_num = max(max_num,n)
temp = [0]
for i in range(1,max_num+1):
    temp.append(temp[-1]+i/(i&-i))
for n in num:
    print(temp[n+1])
    # ans = 0
    # for x in range(1,n+1):
    #     ans+=int(x/(x&-x))
    # res.append(ans)
# for r in res:
#     print(r)

# def f(x):
#     if x % 2 ==1:
#         return 1
#     else:
#         count =0
#         while x %2 !=1:
#             count+=1
#             x//=2
#         return 1<<count

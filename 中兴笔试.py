# n = int(input())
# squre = []
# res = []
# for _ in range(n):
#     temp = list(map(int,input().split()))
#     squre.append(temp)
# squre.sort(key=lambda tup:tup[0])
# for i in range(len(squre)-1,-1,-1):
#     flag = False
#     for j in range(i-1,-1,-1):
#         if squre[i][1] <= squre[j][1]:
#             flag = True
#     if not flag:
#         res.append(squre[i])
# print(len(res))

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2: return s
#         res = ["" for _ in range(numRows)]
#         i, flag = 0, -1
#         for c in s:
#             res[i] += c
#             if i == 0 or i == numRows - 1: flag = -flag
#             i += flag
#         return "".join(res)
# print(Solution().convert("SWORDMAN",4))
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        groups = int(len(s)//((numRows-1)*2) + 1)
        dict = [[""]*numRows for _ in range(groups)]
        for i in range(groups):
            s_i = s[i*groups:(i+1)*groups]
            dict[i]
        print(dict)

print(Solution().convert("SWORDMAN",4))

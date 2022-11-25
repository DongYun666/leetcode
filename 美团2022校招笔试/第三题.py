from collections import Counter
class Solution:
    def Function(self,n,num,S):
        res = [len(Counter(S))]
        S = S[1:]
        for index,s in enumerate(S):
            print(index,s)
            temp = [s]
            num[index]

n = int(input())
num = list(map(int,input().split()))
S = input()
print(Solution().Function(n,num,S))
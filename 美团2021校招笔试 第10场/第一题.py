
class Solution:
    def Elimination_score(self,min_,max_,score):

        score.sort()
        for s in score:
            min_count,max_count = 0,0
            for x in score:
                if x <= s:
                    min_count+=1
                else:
                    max_count+=1
                if min_count>max_ or max_count>max_:
                    break
            if min_<=min_count<=max_ and min_<=max_count<=max_:
                return s
        return -1
n,x,y = list(map(int,input().split()))
num = list(map(int,input().split()))
print(Solution().Elimination_score(x,y,num))

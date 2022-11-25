from collections import Counter, defaultdict
from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        diction = defaultdict(Counter)
        count = defaultdict(int)
        for i in range(len(creators)):
            diction[creators[i]][ids[i]] = views[i]
            count[creators[i]]+=views[i]
        count = sorted(count.items(),key=lambda x: x[1],reverse=True)
        res = []
        t = count[0][1]
        for x,c in count:
            if t == c:
                res.append([x])
            if c<t:
                break
        for index,r in enumerate(res):
            temp = diction["".join(r)]
            temp = sorted(temp.items(),key=lambda x:(-x[1],x[0]))
            res[index].append(temp[0][0])
        return res

creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]

# creators = ["q","p","i"]
# ids = ["sfoj","qqgo","yanl"]
# views = [4,0,4]
# creators = ["alice","alice","alice"]
# ids = ["a","b","c"]
# views = [1,2,2]
print(Solution().mostPopularCreator(creators, ids, views))
from collections import defaultdict, Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = defaultdict(int)
        for w in s:
            d[w]+=1
        for w in t:
            if w in d:
                d[w]-=1
                if d[w] == 0:
                    d.pop(w)
            else:
                d[w]+=1
        return sum(d.values())




s = "leetcode"
t = "coats"
s_map = Counter(s)
t_map = Counter(t)
print(s_map,t_map)
# for key in s_map.keys() | t_map.keys():
#     print(key)
s = "night"
t = "thing"
# print(Solution().minSteps(s, t))


print(type(s_map.keys()))

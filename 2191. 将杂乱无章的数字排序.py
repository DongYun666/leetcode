from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map(x):
            res = 0
            temp = [] if x != 0 else [0]
            while x != 0:
                temp.append(x%10)
                x //= 10
            temp.reverse()
            for t in temp:
                res = res*10 + mapping[t]
            return res
        map_nums = [map(num) for num in nums]
        _,res = zip(*sorted(zip(map_nums,nums),key = lambda x:x[0]))
        return list(res)



mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(Solution().sortJumbled(mapping, nums))
import functools
from typing import List
import heapq

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        s1,s2, = [],[]
        for i in range(len(nums)):
            while len(s2)!=0 and nums[s2[-1]]<nums[i]:
                res[s2.pop()] = nums[i]
            temp = []
            while len(s1)!=0 and nums[s1[-1]]<nums[i]:
                temp.append(s1.pop())
            while len(temp)!=0:
                s2.append(temp.pop())
            s1.append(i)
        return res






nums = [2, 4, 0, 9, 6]
print(Solution().secondGreaterElement(nums))

#         int n = a.size();
#         vector <int> id(n);
#         for (int i = 0; i < n; i++) id[i] = i;
#         sort(id.begin(), id.end(), cmp);
#         vector <int> ans(n, -1);
#         set <int> all;
#         for (int i = 0; i < n; i++) {
#             int j = id[i];
#             auto it = all.lower_bound(j);
#             if (it != all.end()) {
#                 ++it;
#                 if (it != all.end()) ans[j] = a[*it];
#             }
#             all.insert(j);
#         }
#         return ans;
#     }
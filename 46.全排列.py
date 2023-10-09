# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 15:02
# @Author : DongYun
# @File : 46.全排列.py
# @Software : PyCharm
from typing import List


class Solution:
    def permute(self, nums):

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            visit = [0 for i in range(26)]
            for i in range(first, n):
                # 动态维护数组
                if not visit[ord(nums[i])-ord('a')]:
                    visit[ord(nums[i])-ord('a')] = nums[i]
                    nums[first], nums[i] = nums[i], nums[first]
                    # 继续递归填下一个数
                    backtrack(first + 1)
                    # 撤销操作
                    nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
# print(Solution().permute(['a','a','b']))

# s = "123"
# s[0] = "2"
# print(s)




class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        n = len(s)
        res = []
        def dfs(index):
            if index == n:
                res.append("".join(s[:]))
            visited = [0 for i in range(52)]
            for i in range(index,n):
                if not visited[ord(s[i])-ord("a")]:
                    visited[ord(s[i])-ord("a")] = 1
                    s[index],s[i] = s[i],s[index]
                    dfs(index+1)
                    s[index],s[i] = s[i],s[index]
        dfs(0)
        return res

s = "AAB"
print(Solution().permutation(s))
from typing import List

class Tire:
    def __init__(self):
        # 左表示0  右表示1
        self.left = None
        self.right = None

class Solution:
    # 暴力破解
    def findMaximumXOR1(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                res = max(res, nums[i]^nums[j])
        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Tire()
        def builder(num):
            cur = root
            for i in range(30,-1,-1):
                temp = (num >> i) & 1
                if temp == 0:
                    if not cur.left:
                        cur.left = Tire()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Tire()
                    cur = cur.right
        def check(num):
            cur = root
            res = 0
            for i in range(30,-1,-1):
                temp = (num>>i) & 1
                if temp == 0:
                    if cur.right:
                        cur = cur.right
                        res = res*2+1
                    else:
                        cur = cur.left
                        res *= 2
                else:
                    if cur.left:
                        cur = cur.left
                        res = res*2+1
                    else:
                        cur = cur.right
                        res *= 2
            return res


        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = max(res, nums[i] ^ nums[j])
        return res

nums = [3, 10, 5, 2, 8]
print(Solution().findMaximumXOR(nums))
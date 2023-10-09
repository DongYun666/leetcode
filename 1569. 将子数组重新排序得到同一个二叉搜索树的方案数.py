from typing import List
class Solution:
    class TNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.size = 1
            self.ans = 0

    def numOfWays(self, nums: List[int]) -> int:
        def insert(val):
            cur = root
            while True:
                cur.size += 1
                if val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = self.TNode(val)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = self.TNode(val)
                        break
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            leftsize = node.left.size if node.left else 0
            rightsize = node.right.size if node.right else 0

            leftans = node.left.ans if node.left else 1
            rightans = node.right.ans if node.right else 1
            
            node.ans = c[leftsize + rightsize][leftsize] * leftans * rightans % mod
        
        mod = 10 ** 9 + 7
        n = len(nums)
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            c[i][0] = c[i][i] = 1
            for j in range(1, i):
                c[i][j] = c[i - 1][j] + c[i - 1][j - 1] % mod
        
        root = self.TNode(nums[0])
        for val in nums[1:]:
            insert(val)
        dfs(root)
        return (root.ans - 1 + mod)% mod
nums = [3,4,5,1,2]
print(Solution().numOfWays(nums))
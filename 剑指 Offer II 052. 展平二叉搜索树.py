# -*- codeing = utf-8 -*-
# @Time : 2021/12/4 14:21
# @Author : DongYun
# @File : 剑指 Offer II 052. 展平二叉搜索树.py
# @Software : PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        resoult = TreeNode(-1)
        mid = resoult
        def dfs(root):
            nonlocal mid
            if root == None:
                return
            dfs(root.left)
            mid.right = root
            mid.left = None
            mid = root
            dfs(root.right)
        dfs(root)
        return resoult.right



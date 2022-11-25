# -*- codeing = utf-8 -*-
# @Time : 2022/3/9 14:37
# @Author : DongYun
# @File : 面试题32 -1 .从上到下打印二叉树.py
# @Software : PyCharm
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
            res.append(temp)
        return res







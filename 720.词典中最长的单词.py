# -*- codeing = utf-8 -*-
# @Time : 2022/3/17 18:12
# @Author : DongYun
# @File : 720.词典中最长的单词.py
# @Software : PyCharm
from typing import List
class TrieNode(object):
    def __init__(self, value=None, parent=None):
        # 值
        self.value = value
        # 父结点
        self.parent = parent
        # 子节点，{value:TrieNode}
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    #插入结点
    def insert(self, sequence):
        cur_node = self.root
        for item in sequence:
            if item not in cur_node.children:
                # 插入结点
                child = TrieNode(value=item, parent=cur_node)
                cur_node.children[item] = child
                cur_node = child
            else:
                # 更新结点
                cur_node = cur_node.children[item]

    #查询
    def search(self, sequence):
        cur_node = self.root
        mark = True
        for item in sequence:
            if item not in cur_node.children:
                mark = False
                break
            else:
                cur_node = cur_node.children[item]
        # # 如果还有子结点，说明序列并非完整
        # if cur_node.children:
        #     mark = False
        return mark

class Solution1:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        longest = ""
        for word in words:
            # print(t.search(word))
            if t.search(word) and (len(word)>len(longest) or len(word)==len(longest) and word<longest):
                longest = word
        return longest
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None or not node.children[ch].isEnd:
                return False
            node = node.children[ch]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        longest = ""
        for word in words:
            if t.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest



words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution1().longestWord(words))
from typing import List

#字典树
class TreeNode():
    def __init__(self):
        self.nodes = {}
        self.is_leaf = 0
        self.count = 0
    def insert(self,word):
        curr = self
        for w in word:
            if not curr.nodes.get(w,None):
                new_node = TreeNode()
                curr.nodes[w] = new_node
            curr = curr.nodes[w]
        curr.is_leaf +=1
        self.count +=1
        return

    def insert_many(self,words):
        for word in words:
            self.insert(word)
        return
    def search(self,word):
        curr = self
        for w in word:
            if w in curr.nodes:
                curr = curr.nodes[w]
            else:
                return False
        return curr.is_leaf

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        TR = TreeNode()
        TR.insert_many(words)
        res = 0
        temp = ""
        visit = []
        def dfs(index):
            nonlocal temp
            if index == len(s):
                # print(temp)
                t = TR.search(temp)
                if t and temp not in visit:
                    # print(temp)
                    nonlocal res
                    res+=t
                visit.append(temp[:])
                return
            temp += s[index]
            dfs(index+1)
            temp = temp[:-1]
            dfs(index+1)
        dfs(0)
        # print(visit)
        return res




s = "abcde"
words = ["a", "bb", "acd", "ace"]

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

s = "qlhxagxdqh"
words = ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
print(Solution().numMatchingSubseq(s, words))
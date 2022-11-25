from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def check(i,j,k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            vistit.append([i,j])
            res = False
            for d_i,d_j in direction:
                new_i = d_i+i
                new_j = d_j+j
                if -1<new_i<len(board) and -1<new_j<len(board[0]) and [new_i,new_j] not in vistit and check(new_i,new_j,k+1):
                        res = True
                        break
            vistit.remove([i,j])
            return res

        vistit = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i,j,0):
                    return True
        return False

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

board = [['a','b'],['c','d']]
word = "abcd"
print(Solution().exist(board, word))

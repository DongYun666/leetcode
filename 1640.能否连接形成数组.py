from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        temp = [0 for _ in range(len(arr))]
        for piece in pieces:
            if piece[0] not in temp and piece[0] in arr:
                index = arr.index(piece[0])
                temp[index:index+len(piece)] = piece[:]
            else:
                return False
            print(temp)
        return True if temp == arr else False



# arr = [91,4,64,78]
# pieces = [[78],[4,64],[91]]
arr = [49,18,16]
pieces = [[16,18,49]]
print(Solution().canFormArray(arr,pieces))
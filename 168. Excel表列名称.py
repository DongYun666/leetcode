class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 逢26 进1
        res = "" 
        while columnNumber:
            columnNumber -= 1
            res = chr(columnNumber % 26 + 65) + res
            columnNumber //= 26
        return res
columnNumber = 701
columnNumber = 2147483647  
columnNumber = 52
columnNumber = 28
columnNumber = 1
print(Solution().convertToTitle(columnNumber))
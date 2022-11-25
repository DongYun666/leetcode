class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)
        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack
        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"




# num = "1432219"
num = "10200"
num = "10"
# num = "112"
print(Solution().removeKdigits(num,1))
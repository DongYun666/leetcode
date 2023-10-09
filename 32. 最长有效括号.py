from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i-stack[-1])
        return res


s = ")()())"
print(Solution().longestValidParentheses(s))



class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        top = 0
        i = -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1
        return arr


arr = [1,0,2,3,0,4,5,0]
# print(Solution().duplicateZeros(arr))
n = len(arr)
# arr = list("".join(arr).replace("0","00")[:n])
arr = "".join(str(s) for s in arr)
print(arr)
arr = arr.replace("0","00")[:n]
print(arr)
arr = list(int(s) for s in arr)
print(arr)
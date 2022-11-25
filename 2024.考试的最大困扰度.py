# -*- codeing = utf-8 -*-
# @Time : 2022/3/29 10:40
# @Author : DongYun
# @File : 2024.考试的最大困扰度.py
# @Software : PyCharm

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))


answerKey = "TTFTTFTT"
k = 1
# print(Solution().maxConsecutiveAnswers(answerKey,k))
scores = {(2,0): 89, (4,3): 92, (4,4): 93}
print(scores[(2,0)])
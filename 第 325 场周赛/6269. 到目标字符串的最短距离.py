from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = len(words)
        for index,word in enumerate(words):
            if word == target:
                res = min(res, min((startIndex-index+len(words))%len(words),(index - startIndex+len(words))%len(words)))
        return res if res != len(words) else -1

words = ["hello", "i", "am", "leetcode", "hello"]
target = "hello"
startIndex = 1

# words = ["a","b","leetcode"]
# target = "leetcode"
# startIndex = 0
#
words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8
print(Solution().closetTarget(words, target, startIndex))
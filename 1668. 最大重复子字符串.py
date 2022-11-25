from typing import List

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        temp = word
        while word in sequence:
            word+=temp
            res+=1
        return res


sequence = "ababc"
word = "ab"

# sequence = "ababc"
# word = "ba"

# sequence = "ababc"
# word = "ac"

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

# sequence = "a"
# word = "a"
print(Solution().maxRepeating(sequence, word))
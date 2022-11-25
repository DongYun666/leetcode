from collections import Counter, defaultdict
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        temp = []
        res = []
        for index,word in enumerate(words):
            t = []
            for i in range(1,len(word)):
                t.append(ord(word[i])- ord(word[i-1]))
            if len(temp) == 0 or t not in temp:
                temp.append(t)
                res.append(word)
            elif t in temp and len(temp) == 2:
                if t == temp[0]:
                    return res[1]
                else:
                    return res[0]
        return words[-1]


words = ["adc","wzy","abc"]
# words = ["aaa","bob","ccc","ddd"]
words = ["mll","edd","jii","tss","fee","dcc","nmm","abb","utt","zyy","xww","tss","wvv","xww","utt"]
print(Solution().oddString(words))
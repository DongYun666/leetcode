from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(word):
            i = j = 0
            if len(word)>len(s):
                return False
            while j < len(s) and i < len(word):
                if s[j]!= word[i]:
                    return False
                cur = s[j]
                cur_cnt_j = 0
                cur_cnt_i = 0
                while j < len(s):
                    if s[j] == cur:
                        cur_cnt_j+=1
                        j+=1
                    else:
                        break
                while i < len(word):
                    if word[i] == cur:
                        cur_cnt_i+=1
                        i+=1
                    else:
                        break
                if cur_cnt_i == cur_cnt_j:
                    continue
                if cur_cnt_j <=2 or cur_cnt_j < cur_cnt_i:
                    return False
            return True if j == len(s) and i == len(word) else False
        return sum(check(word) for word in words)

s = "heeellooo"
words = ["hello", "hi", "helo"]

# s = "abcd"
# words = ["abc"]
print(Solution().expressiveWords(s, words))
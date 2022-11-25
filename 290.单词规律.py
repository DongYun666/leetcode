from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_ch = defaultdict()
        ch_word = defaultdict()
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        for word,ch in zip(pattern,s_list):
            if word in word_ch and word_ch[word]!=ch or ch in ch_word and ch_word[ch]!=word:
                return False
            word_ch[word] = ch
            ch_word[ch] = word
        return True





pattern = "abba"
s = "dog dog dog dog"
print(Solution().wordPattern(pattern,s))
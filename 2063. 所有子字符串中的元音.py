class Solution:
    def countVowels(self, word: str) -> int:
        # 先对word进行预处理，如果是元音字母 标注为1 否则为0
        res = 0
        n = len(word)
        for i in range(len(word)):
            if word[i] in "aeiou":
                res += (i + 1) * (n - i)
        return res
    
word = "aba"

word = "abc"

word = "ltcd"

word = "noosabasboosa"
print(Solution().countVowels(word))
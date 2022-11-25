# -*- codeing = utf-8 -*-
# @Time : 2021/12/4 8:25
# @Author : DongYun
# @File : 383.赎金信.py
# @Software : PyCharm
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)
        for ch in ransomNote_counter:
            magazine_counter[ch]-=ransomNote_counter[ch]
            if magazine_counter[ch] <0:
                return False
        return True
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch,"",1)
        return True
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
print(Solution().canConstruct4("aa","aab"))
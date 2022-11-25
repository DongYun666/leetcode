from collections import Counter
class Solution:
    def canConstruct(self, randomNote: str, magazine: str) -> bool:
        return not Counter(randomNote) - Counter(magazine)




randomNote = "b"
magazine = "aab"
print(Solution().canConstruct(randomNote,magazine))
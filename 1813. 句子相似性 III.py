class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        i,j = 0,0
        while i < len(sentence1) and i < len(sentence2) and sentence1[i] == sentence2[i]:
            i += 1
        while j < len(sentence1)-i and j < len(sentence2)-i and sentence1[-j-1] == sentence2[-j-1]:
            j += 1
        return i+j == min(len(sentence1),len(sentence2))

sentence1 = "My name is Haley"
sentence2 = "My Haley"

sentence1 = "of"
sentence2 = "A lot of words"

sentence1 = "Eating right now"
sentence2 = "Eating"

sentence1 = "Luky"
sentence2 = "Lucccky"

sentence1 = "Ogn WtWj HneS"
sentence2 = "Ogn WtWj HneS"

print(Solution().areSentencesSimilar(sentence1, sentence2))
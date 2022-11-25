class Solution:
    def reorderSpaces(self, text: str) -> str:
        t = text.split()
        space_count = text.count(' ')
        if len(t) == 1:
            return "".join(t[0])+" "*space_count
        return (' '*(space_count//(len(t)-1))).join(t)+" "*(space_count % (len(t)-1))

text = "  this   is  a sentence "
print(Solution().reorderSpaces(text))

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [i for i in s if i != ""]
        s = s[::-1]
        print(s)
        return " ".join(s)
    
s = "  hello world  "
print(Solution().reverseWords(s))
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a in b:
            first = b.index(a)
        else:
            return -1
        res = 0
        for i in range(first,len(b)-len(a),len(a)):
            if b[i:len(a)+i] == a:
                res+=1
        return res+1






a = "abcd"
b = "cdabcdabcd"

a = "a"
b = "a"

a = "abc"
b = "wxyz"
print(Solution().repeatedStringMatch(a, b))
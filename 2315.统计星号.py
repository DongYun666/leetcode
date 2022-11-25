class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        print(s)
        res = 0
        for i in range(0,len(s),2):
            print(i)
            res+=s[i].count("*")
        res+=s[len(s)-1].count("*") if not len(s)%2 else 0
        return res


s = "l|*e*et|c**o|*de|***|wewe|23we*"
print(Solution().countAsterisks(s))
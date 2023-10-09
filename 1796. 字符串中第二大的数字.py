class Solution:
    def secondHighest(self, s: str) -> int:
        first,second = -1,-1
        for c in s:
            if c.isdigit():
                t = int(c)
                if t > first:
                    second = first
                    first = t
                elif second<t<first:
                    second = t
        return second




s = "dfa12321afd"
print(Solution().secondHighest(s))
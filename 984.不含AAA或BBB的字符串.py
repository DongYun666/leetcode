class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a or b:
            if len(res)>1 and res[-1] == res[-2]:
                w_a = res[-1] == 'b'
            else:
                w_a = a>b
            if w_a:
                a-=1
                res.append('a')
            else:
                b-=1
                res.append('b')
        return res

a = 1
b = 2
print(Solution().strWithout3a3b(a,b))
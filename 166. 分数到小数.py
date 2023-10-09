class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0: return str(numerator // denominator)
        ans = []
        if (numerator < 0) ^ (denominator < 0): ans.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        ans.append(str(numerator // denominator) + '.')
        numerator %= denominator
        index = len(ans)
        table = {}
        while numerator:
            if numerator in table:
                ans.insert(table[numerator], '(')
                ans.append(')')
                break
            table[numerator] = index
            numerator *= 10
            ans.append(str(numerator // denominator))
            numerator %= denominator
            index += 1
        return ''.join(ans)
numerator = 4
denominator = 333
print(Solution().fractionToDecimal(numerator, denominator))
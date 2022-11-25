class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        res = []



numerator = 4
denominator = 333
print(Solution().fractionToDecimal(numerator, denominator))
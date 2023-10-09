class Solution:
    def largestPalindrome(self, n: int) -> int: 
        if n == 1:
            return 9
        mod = 1337
        max_num = 10 ** n - 1
        min_num = 10 ** (n - 1)
        for i in range(max_num, min_num, -1):
            s = str(i)
            num = int(s + s[::-1])
            for j in range(max_num, min_num, -1):
                if num // j > max_num:
                    break
                if num % j == 0:
                    return num % mod
        return -1
    

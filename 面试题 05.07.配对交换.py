class Solution:
    def exchangeBits(self, num: int) -> int:
        return num ^ (2**(len(bin(num))-2)-1)




num = 3
print(Solution().exchangeBits(num))
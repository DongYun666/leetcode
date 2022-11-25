class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def count(num):
            res = 0
            if num <= 9:
                return num
            else:
                return count(num//10)+num%10
        if count(n)<=target:
            return 0
        i = 1
        while True:
            temp = n
            num = (temp//i+1)*i
            if count(num)<=target:
                return num-n
            i*=10




n = 16
target = 6

n = 467
target = 6
print(Solution().makeIntegerBeautiful(n, target))
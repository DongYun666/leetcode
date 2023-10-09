class Solution:
    def minimumBoxes(self, n: int) -> int:
        sub_sum = 0
        i = 1
        while sub_sum+i*(i+1)//2 < n:
            sub_sum += i*(i+1)//2
            i+=1
        diff = n-sub_sum
        for x in range(1,i+1):
            diff -= x
            if diff <=0:
                break
        return x+i*(i-1)//2


n = 15
print(Solution().minimumBoxes(n))
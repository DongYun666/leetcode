from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_d = 1
        res = 0
        while 10**n_d<=n:
            res+=(len(digits))**n_d
            n_d+=1

        def bisearch(arr, x):
            if x < arr[0]:
                return 0
            if x > arr[-1]:
                return len(arr)
            left, right = -1, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    right = mid
                else:
                    left = mid + 1
            return left
        flag = True
        if n%10!=0:
            digits = [int(x) for x in digits]
            if bisearch(digits,n//10**(n_d-1)) == 0:
                return res
            else:
                while n != 0:
                    if n//(10**(n_d-1)) not in digits:
                        flag = False
                    temp = bisearch(digits,n//(10**(n_d-1)))
                    if temp!=0:
                        res+=temp*len(digits)**(n_d-1)
                    n-=n//(10**(n_d-1))*(10**(n_d-1))
                    n_d-=1
            return res+1 if flag else res
        else:
            return res



digits = ["1", "3", "5", "7"]
digits = ['7']
# digits = ["1","4","9"]
# digits = ["3","4","5","6"]
n = 8

# n = 1000000000
print(Solution().atMostNGivenDigitSet(digits, n))
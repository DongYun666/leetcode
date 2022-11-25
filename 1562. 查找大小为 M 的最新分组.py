from typing import List

class Solution:

    #超时
    def findLatestStep(self, arr: List[int], m: int) -> int:
        target = (1<<len(arr))-1
        def exists(num,index):
            num_s = bin(num)[2:]
            i,j = index-1,index+1
            l_1,r_1 = 0,0
            while i>=1 and num_s[i] == "1" and l_1 <= m:
                l_1+=1
                i -=1
            while j<len(num_s) and num_s[j] == "1" and r_1 <= m:
                r_1+=1
                j +=1
            return l_1 == m or r_1 == m

        for index,num in enumerate(arr[::-1]):
            if target == (1<<m)-1:
                return len(arr)
            if exists(target,num-1):
                return len(arr)-index
            target ^= 1<<len(arr)-num
        return -1
        # print(1<<0)
        # print(target.bit_length())
        # print((1<<5)-1)



arr = [3, 5, 1, 2, 4]
m = 1

arr = [1]
m = 1

arr = [2,1]
m = 2

arr = [3,1,5,4,2]
m = 2

arr = [1,2]
m = 1
print(Solution().findLatestStep(arr, m))

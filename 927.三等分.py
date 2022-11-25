from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        arr_sum = sum(arr)
        if arr_sum == 0:
            return [0, 1]
        if arr_sum % 3 !=0:
            return [-1, -1]
        target_sum = arr_sum//3
        #求第三部分
        cnt = 0
        for j in range(len(arr)-1,-1,-1):
            if arr[j] == 1:
                cnt+=1
            if cnt == target_sum:
                break
        reanl_length = len(arr)-j
        real_arr = arr[j:len(arr)]
        i= 0
        while arr[i] == 0:
            i+=1
        if arr[i:i+reanl_length] != real_arr:
            return [-1, -1]
        i = i+reanl_length
        k = i
        while arr[k] == 0:
            k+=1
        if arr[k:k+reanl_length] != real_arr:
            return [-1,-1]
        k = k+reanl_length
        return [i-1,k]














arr = [1,0,1,0,1]
print(Solution().threeEqualParts(arr))
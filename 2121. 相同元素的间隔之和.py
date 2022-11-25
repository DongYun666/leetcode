from collections import defaultdict
from typing import List

class Solution:
    def getDistances1(self, arr: List[int]) -> List[int]:
        dict = defaultdict(list)
        for index,num in enumerate(arr):
            dict[num].append(index)
        res = [0]*len(arr)
        def count(index,nums):
            ans = 0
            diff = [0]
            index = nums.index(index)
            for i in range(1,len(nums)):
                diff.append(nums[i]-nums[i-1])
            t = 1
            for i in range(1,index+1):
                ans+=t*diff[i]
                t+=1
            t = 1
            for i in range(len(nums)-1,index,-1):
                ans+=t*diff[i]
                t+=1
            return ans

        for i in range(len(arr)):
            temp = dict[arr[i]]
            res[i] = count(i,temp)
        return res

    def getDistances(self, arr: List[int]) -> List[int]:
        dict1 = defaultdict(list)
        re1 = [0]*len(arr)
        for i in range(len(arr)):
            temp = dict1[arr[i]] if dict1.get(arr[i]) else [0,0]
            if temp[1]!=0:
                re1[i] = re1[temp[0]]+(i-temp[0])*temp[1]
            temp[0] = i
            temp[1] +=1
            dict1[arr[i]] = temp

        dict2 = defaultdict(list)
        re2 = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            temp = dict2[arr[i]] if dict2.get(arr[i]) else [0, 0]
            if temp[1] != 0:
                re2[i] += re2[temp[0]] + (temp[0] - i) * temp[1]
            temp[0] = i
            temp[1] += 1
            dict2[arr[i]] = temp
        print(re1,re2)
        res = [0]*len(arr)
        for i in range(len(re1)):
            res[i] = re1[i]+re2[i]
        return res

arr = [2, 1, 3, 1, 2, 3, 3]
print(Solution().getDistances(arr))








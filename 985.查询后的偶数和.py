from typing import List
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if not num & 1)
        res = []
        for i in range(len(queries)):
            temp_sum = queries[i][0] + nums[queries[i][1]]
            if temp_sum & 1:
                if not nums[queries[i][1]] & 1:
                    even_sum-=nums[queries[i][1]]
            else:
                if nums[queries[i][1]] & 1:
                    even_sum+=temp_sum
                else:
                    even_sum+=queries[i][0]
            nums[queries[i][1]] = temp_sum
            res.append(even_sum)
        return res





A= [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(Solution().sumEvenAfterQueries(A, queries))
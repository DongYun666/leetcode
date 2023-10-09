from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for num in nums:
                if num in track:
                    continue
                track.append(num)
                backtrack(nums,track)
                track.pop()
        backtrack(nums,[])
        return res
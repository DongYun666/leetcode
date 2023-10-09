import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap,num)

        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

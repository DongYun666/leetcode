from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memory = {1:[1]}
        def f(n):
            if n not in memory:
                odds = f((n+1)//2)
                evens = f(n//2)
                memory[n] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memory[n]
        return f(n)



n = 5
print(Solution().beautifulArray(n))
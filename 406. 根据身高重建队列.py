from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0],x[1]))
        res = list()
        for person in people:
            res[person[1]:person[1]] = [person]
        return res
    
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))
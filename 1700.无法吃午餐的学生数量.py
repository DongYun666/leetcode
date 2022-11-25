from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = sum(students)
        s0 = len(students)-s1
        for i in sandwiches:
            if i == 0 and s0:
                s0 -=1
            elif i == 1 and s1:
                s1-=1
            else:
                break
        return s0+s1





students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(Solution().countStudents(students, sandwiches))
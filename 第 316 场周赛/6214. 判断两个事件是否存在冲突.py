from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_t,event2_t = [],[]
        for time in event1:
            temp = time.split(":")
            event1_t.append(int(temp[0])*60+int(temp[1]))
        for time in event2:
            temp = time.split(":")
            event2_t.append(int(temp[0])*60+int(temp[1]))
        return event2_t[0]<=event1_t[1]<=event2_t[1] or event1_t[0]<=event2_t[1]<=event1_t[1]

event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]
event1 = ["10:00","11:00"]
event2 = ["14:00","15:00"]
print(Solution().haveConflict(event1, event2))
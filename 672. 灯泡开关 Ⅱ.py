class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n ==2:
            return 3 if presses == 1 else 4
        else:
            if presses ==1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8
            
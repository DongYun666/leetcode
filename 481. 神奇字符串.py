class Solution:
    def magicalString(self, n: int) -> int:
        s = [1,2,2]
        count = 1
        i,j = 2,2
        if n <= 3:
            return 1
        while j<=(n-2):
            if s[j] == 2:
                s += [1] * s[i]
                if j == n-2:
                    count+=1
                else:
                    count+=s[i]
            else:
                s +=[2]*s[i]
            j+=s[i]
            i+=1
        return count



n = 4
print(Solution().magicalString(n))
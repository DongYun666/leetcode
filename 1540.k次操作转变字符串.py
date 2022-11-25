class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        record = []
        for i in range(len(s)):
            diff= ord(t[i]) - ord(s[i])
            diff = diff if diff>=0 else diff+26
            if diff == 0:
                continue
            else:
                if diff not in record:
                    record.append(diff)
                else:
                    while diff+26 <= k:
                        diff += 26
                        if diff not in record:
                            record.append(diff)
                            continue
                    if diff > k:
                        return False
        return True

s = "abc"
t = "bcd"
k = 10
print(Solution().canConvertString(s,t,k))
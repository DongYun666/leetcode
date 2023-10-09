
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False for i in range(n)]
        dp[0] = True
        cnt = 1
        for i in range(minJump,n):
            if s[i] == "0" and cnt > 0:
                dp[i] = True
            if i >= maxJump and dp[i-maxJump]:
                cnt -= 1
            if dp[i-minJump+1]:
                cnt += 1
        return dp[-1]


s = "011010"
minJump = 2
maxJump = 3

# s = "01"
# minJump = 1
# maxJump = 1
print(Solution().canReach(s, minJump, maxJump))
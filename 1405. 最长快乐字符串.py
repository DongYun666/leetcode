class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        cnt = [[a,'a'],[b,'b'],[c,'c']]
        while True:
            cnt = sorted(cnt,key=lambda x:x[0],reverse=True)
            flag = False
            for index,(num,ch) in enumerate(cnt):
                if num == 0:
                    break
                if len(res) >= 2 and res[-1] == res[-2] == ch:
                    continue
                flag = True
                res.append(ch)
                cnt[index][0] -= 1
                break
            if not flag:
                return ''.join(res)
a = 1
b = 1
c = 7

a = 2
b = 2
c = 1
print(Solution().longestDiverseString(a,b,c))

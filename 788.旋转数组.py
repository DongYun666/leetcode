class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0,0,1,-1,-1,1,1,-1,0,1]
        ans = 0
        for i in range(1,n+1):
            valid,diff = True,False
            i_l = [int(j) for j in str(i)]
            for num in i_l:
                if check[num] == -1:
                    valid = False
                    break
                elif check[num] == 1:
                    diff = True
            if valid and diff:
                ans+=1
        return ans





n =  10
print(Solution().rotatedDigits(n))
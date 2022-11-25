class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # 获取对应的进制
        def get_base(n,base):
            resoult = ""
            while n:
                resoult = str(n%base)+resoult
                n//=base
            return resoult
        #判断回文
        def is_palindrome(s):
            left,right = 0,len(s)-1
            while left < right:
                if s[left] == s[right]:
                    left+=1
                    right-=1
                    continue
                else:
                    return False
            return True
        for i in range(2,n-1):
            # 获取对应的jinzhi
            resoult = get_base(n,i)
            #判断回文
            if not is_palindrome(resoult):
                return False
        return True

n = 9
print(Solution().isStrictlyPalindromic(n))

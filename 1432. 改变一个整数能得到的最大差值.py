class Solution:
    def maxDiff(self, num: int) -> int:
        num_max = num_min = str(num)
        for n in num_max:
            if n != "9":
                num_max = num_max.replace(n,"9")
                break

        for i, n in enumerate(num_min):
            if i == 0:
                if n != "1":
                    num_min = num_min.replace(n,"1")
                    break
            else:
                if n != num_min[0]:
                    num_min = num_min.replace(n,"0")
                    break

        return int(num_max)-int(num_min)


num = 9288
num = 555
print(Solution().maxDiff(num))
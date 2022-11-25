import sys
if __name__ == "__main__":
    def canjump(nums):
        n = len(nums)
        rightmost = nums[0]
        for i in range(n):
            if i < rightmost:
                rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
        return False

    N = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums = list(map(int,line.split()))
    flag = canjump(nums)
    print(flag)
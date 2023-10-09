import sys
from collections import defaultdict
#使用双指针求解最长不重复子串
def max_val(nums):
    if not nums:
        return 0
    max_length = 0
    left,right = 0,0
    record = []
    while right < len(nums):
        if nums[right] not in record:
            record.append(nums[right])
            right += 1
            max_length = max(max_length,right - left)
        else:
            record.remove(nums[left])
            left += 1
            
    return max_length

if __name__ == '__main__':
    for line in sys.stdin:
        nums = list(map(int,line.split()))
        resoult = max_val(nums)
        print(resoult)
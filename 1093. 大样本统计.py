from typing import List
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min_ = 256
        max_ = 0
        sum_ = 0
        sum_count = 0
        mode = 0
        for i in range(len(count)):
            if count[i] != 0:
                min_ = min(min_, i)
                max_ = max(max_, i)
                sum_ += i * count[i]
                sum_count += count[i]
                mode = max(mode, i ) if count[i] > count[mode] else mode
        mean = sum_ / sum_count
        def find_median(count, t):
            median_count = 0
            for i in range(len(count)):
                median_count += count[i]
                if median_count >= t:
                    return i
        median = find_median(count, sum_count // 2 + 1) if sum_count % 2 == 1 else (find_median(count, sum_count // 2) + find_median(count, sum_count // 2 + 1)) / 2
        return [min_, max_, mean, median, mode]
    
count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(Solution().sampleStats(count))
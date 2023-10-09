from collections import defaultdict
from typing import List
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        # 按照出现次数排序
        c_dict = defaultdict(int)
        for i in barcodes:
            c_dict[i] += 1
        c_dict = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)
        index = 0
        for k,v in c_dict:
            barcodes[index:index+v] = [k]*v
            index += v
        res = [0] * len(barcodes)
        # 从头开始，每隔一个填充一个
        length = len(barcodes)
        res[::2] = barcodes[:length // 2 + length % 2]
        # 剩下的填充
        res[1::2] = barcodes[len(barcodes) // 2 + length % 2:]
        return res
barcodes = [1,1,1,2,2,2,3]
# barcodes = [1,2,1]
# barcodes = [1,1,2]
# barcodes = [2,2,1,3]
print(Solution().rearrangeBarcodes(barcodes))
# -*- codeing = utf-8 -*-
# @Time : 2022/7/10 10:20
# @Author : DongYun
# @File : 第二题.py
# @Software : PyCharm
from typing import List
class SmallestInfiniteSet:

    def __init__(self):
        self.num_list = [i for i in range(100)]
    def popSmallest(self) -> int:
        print(self.num_list[0])
        self.num_list.pop(0)
    def addBack(self, num: int) -> None:
        if num not in self.num_list:
            self.num_list.append(num)
        self.num_list.sort()

if  __name__ == "__main__":
    smallestInfiniteSet = SmallestInfiniteSet()
    smallestInfiniteSet.addBack(2);    # 2 已经在集合中，所以不做任何变更。
    smallestInfiniteSet.popSmallest(); # 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
    smallestInfiniteSet.popSmallest(); # 返回 2 ，并将其从集合中移除。
    smallestInfiniteSet.popSmallest(); # 返回 3 ，并将其从集合中移除。
    smallestInfiniteSet.addBack(1);    # 将 1 添加到该集合中。
    smallestInfiniteSet.popSmallest(); # 返回 1 ，因为 1 在上一步中被添加到集合中，
                                       # 且 1 是最小的整数，并将其从集合中移除。
    smallestInfiniteSet.popSmallest(); # 返回 4 ，并将其从集合中移除。
    smallestInfiniteSet.popSmallest(); # 返回 5 ，并将其从集合中移除。
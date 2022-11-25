from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ps = []
        for rect in rectangles:
            ps.append(rect[0])
            ps.append(rect[2])
        ps.sort()
        ans = 0
        for i in range(1,len(ps)):
            a,b = ps[i-1],ps[i]
            width = b-a
            if width == 0:
                continue
            lines = [(info[1],info[3])for info in rectangles if info[0]<=a and b <=info[2]]
            lines.sort()
            height,l,r = 0,-1,-1
            for cur in lines:
                if cur[0]>r:
                    height +=r-l
                    l,r = cur
                elif cur[1]>r:
                    r = cur[1]
            height +=r-l
            ans += height * width
        return ans % 1000000007
#
# class Solution:
#     def rectangleArea(self, rs: List[List[int]]) -> int:
#         ps = []
#         for info in rs:
#             ps.append(info[0])
#             ps.append(info[2])
#         ps.sort()
#         ans = 0
#         for i in range(1, len(ps)):
#             a, b = ps[i - 1], ps[i]
#             width = b - a
#             if width == 0:
#                 continue
#             lines = [(info[1], info[3]) for info in rs if info[0] <= a and b <= info[2]]
#             lines.sort()
#             height, l, r = 0, -1, -1
#             for cur in lines:
#                 if cur[0] > r:
#                     height += r - l
#                     l, r = cur
#                 elif cur[1] > r:
#                     r = cur[1]
#             height += r - l
#             ans += height * width
#         return ans % 1000000007



rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
print(Solution().rectangleArea(rectangles))
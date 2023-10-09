class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 - abs(radius)<=xCenter<= x2 + abs(radius) and y1 - abs(radius) <=yCenter<= y2 + abs(radius):
            # 如果园在 四个 角上
            if xCenter < x1 and yCenter > y2 or xCenter < x1 and yCenter < y1 or xCenter > x2 and yCenter > y2 or xCenter > x2 and yCenter < y1:
                return (x1 - abs(radius) - xCenter)**2 + (yCenter - y2 - abs(radius))**2 <= radius**2
            return True
        
        return False
    
radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1

radius = 24
xCenter = 13
yCenter = 1
x1 = 0
y1 = 15
x2 = 5
y2 = 18

print(Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
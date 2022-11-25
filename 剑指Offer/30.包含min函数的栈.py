# -*- codeing = utf-8 -*-
# @Time : 2022/3/4 10:37
# @Author : DongYun
# @File : 30.包含min函数的栈.py
# @Software : PyCharm
#采用辅助栈的思路
class MinStack:

    def __init__(self):
        self.A,self.B=[],[]

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1]>=x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
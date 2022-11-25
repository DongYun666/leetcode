# -*- codeing = utf-8 -*-
# @Time : 2022/3/4 10:25
# @Author : DongYun
# @File : 9.用两个栈实现队列.py
# @Software : PyCharm
class CQueue:

    def __init__(self):
        self.A,self.B=[],[]
    def appendTail(self, value: int) -> None:
        self.A.append(value)
    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

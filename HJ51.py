# -*- codeing = utf-8 -*-
# @Time : 2022/4/14 22:02
# @Author : DongYun
# @File : HJ51.py
# @Software : PyCharm


class Node():
    def __init__(self, val=0):
        self.val = val
        self.next = None
while True:
    try:
        head = Node()
        p = head
        N = int(input())
        num_list = list(map(int, input().split()))
        key = int(input())
        for i in range(len(num_list)):
            node = Node(num_list[i])
            p.next = node
            p = node
        q = head.next
        pre = head
        while q != None:
            n = q.next
            q.next = pre
            pre = q
            q = n
            if n!=None:
                n = n.next
        while pre!=head and key != 1:
            key-=1
            pre = pre.next
        print(pre.val)
    except:
        break
# -*- codeing = utf-8 -*-
# @Time : 2021/12/3 16:56
# @Author : DongYun
# @File : 面试题 02.08.环路检测.py
# @Software : PyCharm
from warehouse.LinkList import Node,SingleLinkList

class Solution:
    def detectCycle(self, head: Node) -> Node:
        slow,fast = head,head
        while fast != None:
            slow = slow.next
            if fast.next == None:
                return None
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

if __name__ == '__main__':
    SingleLinkList = SingleLinkList([1,2,3,4,5,6,7])
    SingleLinkList.show()
    p = SingleLinkList.getHead()
    while p.next != None:
        p = p.next
    p.next = SingleLinkList.getHead().next
    # SingleLinkList.show()
    print(Solution().detectCycle(SingleLinkList.getHead()))
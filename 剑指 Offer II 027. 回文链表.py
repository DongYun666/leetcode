# -*- codeing = utf-8 -*-
# @Time : 2021/12/6 17:38
# @Author : DongYun
# @File : 剑指 Offer II 027. 回文链表.py
# @Software : PyCharm
from warehouse.LinkList import SingleLinkList,Node

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        quit,slow = head,head
        # 让快指针先走到末尾，此时的慢指针在链表中间
        while quit.next != None:
            if quit.next.next:
                quit = quit.next.next
            else:
                break
            slow = slow.next
        x =self.reverse_list(slow.next)

        self.reverse_list(x)


    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous




if __name__ == '__main__':
    link = SingleLinkList([1,2,3,4])
    link.show()
    print(Solution().isPalindrome(link.getHead()))

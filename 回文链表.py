# -*- codeing = utf-8 -*-
# @Time : 2021/12/6 18:55
# @Author : DongYun
# @File : 回文链表.py
# @Software : PyCharm
from warehouse.LinkList import SingleLinkList,Node
class Solution:

    def isPalindrome(self, head: Node) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.elem != second_position.elem:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

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
    link = SingleLinkList([1,2,3,4,5])
    link.show()

    # print(Solution().reverse_list(link.getHead()))
    def printlink(head):
        while head.next is not None:
            print(head.elem,end=" -> ")
            head = head.next
        print(head.elem)
    printlink(Solution().reverse_list(link.getHead()))
    print(Solution().isPalindrome(link.getHead()))
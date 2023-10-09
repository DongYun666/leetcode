import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0,head)
        p = res.next
        while p.next:
            temp = ListNode(val = math.gcd(p.val,p.next.val))
            post = p.next
            p.next = temp
            temp.next = post
            p = post
        return res.next
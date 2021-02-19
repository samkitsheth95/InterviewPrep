# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()
        curr, carry = dummyHead, 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            val = l1.val + l2.val + carry
            carry = 0
            if val >= 10:
                carry = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummyHead.next
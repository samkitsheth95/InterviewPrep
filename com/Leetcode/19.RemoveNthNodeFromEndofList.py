# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        rIndex = head
        j = 0
        while current.next:
            current = current.next
            j += 1
            if j > n:
                rIndex = rIndex.next
        if j < n:
            head = head.next
        else:
            rIndex.next = rIndex.next.next
        return head

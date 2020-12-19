# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fakeHead = ListNode()
        fakeHead.next = head
        curr = fakeHead
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
                continue
            curr = curr.next
        return fakeHead.next
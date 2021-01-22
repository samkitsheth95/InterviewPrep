# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def customReverse(self, currNode: ListNode, k: int) -> ListNode:
        temp = currNode
        prevNode = None
        while currNode and k:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            k -= 1
        temp.next = currNode
        return prevNode

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(0, head)
        moves = n - m + 1
        curr = dummyHead
        for i in range(m - 1):
            curr = curr.next
        curr.next = self.customReverse(curr.next, moves)
        return dummyHead.next

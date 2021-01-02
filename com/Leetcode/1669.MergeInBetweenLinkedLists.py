# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        fakeNode = ListNode()
        fakeNode.next = list1
        list1Curr = fakeNode
        list2Curr = list2
        aPos, bPos = None, None
        temp = 0

        while list1Curr.next:
            if temp == a:
                aPos = list1Curr
            if temp == b:
                bPos = list1Curr.next
                break
            list1Curr = list1Curr.next
            temp += 1

        while list2Curr.next:
            list2Curr = list2Curr.next

        aPos.next = list2
        list2Curr.next = bPos.next

        return fakeNode.next

    def mergeInBetweenForLoop(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        fakeNode = ListNode(next=list1)
        list1Curr = fakeNode
        list2Curr = list2
        aPos, bPos = None, None

        for i in range(b + 1):
            if i == a:
                aPos = list1Curr
            list1Curr = list1Curr.next
        bPos = list1Curr

        while list2Curr.next:
            list2Curr = list2Curr.next

        aPos.next = list2
        list2Curr.next = bPos.next
        return fakeNode.next

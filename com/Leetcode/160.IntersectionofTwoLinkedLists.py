# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getIntersectionNodeSet(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA, currB = headA, headB
        setA = set()

        while currA:
            setA.add(currA)
            currA = currA.next

        while currB:
            if currB in setA:
                return currB
            currB = currB.next

        return None

    def moveForwardByDiff(self, head, diff):
        while diff:
            head = head.next
            diff -= 1
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        currA, currB = headA, headB

        while currA:
            currA = currA.next
            lenA += 1

        while currB:
            currB = currB.next
            lenB += 1

        if lenA > lenB:
            currA = self.moveForwardByDiff(headA, lenA - lenB)
            currB = headB
        else:
            currB = self.moveForwardByDiff(headB, lenB - lenA)
            currA = headA

        while currA:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None

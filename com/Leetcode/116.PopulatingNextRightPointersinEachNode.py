from collections import deque


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connectNaive(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = deque([root])
        while q:
            size = len(q)

            while size:
                curr = q.popleft()
                size -= 1
                if size:
                    curr.next = q[0]
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root
    
    def connectSmart(self, root: 'Node') -> 'Node':
        if not root:
            return
        leftNode = root
        while leftNode.left:
            head = leftNode
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftNode = leftNode.left
        return root

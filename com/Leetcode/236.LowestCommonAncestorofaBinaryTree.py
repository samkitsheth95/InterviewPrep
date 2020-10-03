# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:

    def lowestCommonAncestorR(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right:
            return root
        if not left and not right:
            return
        return left if left else right

    def lowestCommonAncestorI(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound, qFound = False, False
        pNodes = {}
        queue = deque()
        queue.append(root)
        pNodes[root] = None
        while p not in pNodes or q not in pNodes:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
                pNodes[current.left] = current
            if current.right:
                queue.append(current.right)
                pNodes[current.right] = current
        allp = set()
        while p:
            allp.add(p)
            p = pNodes[p]
        while q not in allp:
            q = pNodes[q]
        return q

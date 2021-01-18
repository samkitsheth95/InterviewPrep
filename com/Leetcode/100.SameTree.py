from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isSameTreeRecursive(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
        elif not p and not q:
            return True
        else:
            return False

    def isSameTree(self, p: TreeNode, qn: TreeNode) -> bool:
        q = deque()
        q.append((p, qn))
        while q:
            pCurr, qCurr = q.popleft()
            if (pCurr and qCurr) and (pCurr.val == qCurr.val):
                q.append((pCurr.left, qCurr.left))
                q.append((pCurr.right, qCurr.right))
            elif not pCurr and not qCurr:
                continue
            else:
                return False
        return True

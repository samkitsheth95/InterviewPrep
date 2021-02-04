# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def findNode(root: TreeNode):
            if not root:
                return
            if root.val == t.val and areSame(root, t):
                return True
            return findNode(root.left) or findNode(root.right)

        def areSame(p: TreeNode, q: TreeNode):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return areSame(p.left, q.left) and areSame(p.right, q.right)

        return findNode(s)

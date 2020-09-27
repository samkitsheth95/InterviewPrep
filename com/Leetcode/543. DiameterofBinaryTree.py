# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = 0

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.ans = max(self.ans, right + left)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root)
        return self.ans

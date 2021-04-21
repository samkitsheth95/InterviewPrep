# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertIntoBSTIterative(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if not root:
            return newNode
        curr = root
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        if val > prev.val:
            prev.right = newNode
        else:
            prev.left = newNode
        return root

    def insertIntoBSTIterative(self, root: TreeNode, val: int) -> TreeNode:
        newNode, curr = TreeNode(val), root
        while curr:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    return root
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    return root
        return newNode
    
    def insertIntoBSTRecursive(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

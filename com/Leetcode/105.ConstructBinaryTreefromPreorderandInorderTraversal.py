# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTreeNaive(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        value = preorder.pop(0)
        root = TreeNode(value)

        idx = inorder.index(value)

        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])

        return root

    def buildTreeNaiveConsise(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

    def buildTreeLeetcode(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i

        def helper(left, right):
            nonlocal preIdx

            if left == right:
                return None

            root = TreeNode(preorder[preIdx])
            idx = lookup[preorder[preIdx]]

            preIdx += 1
            root.left = helper(left, idx)
            root.right = helper(idx + 1, right)
            return root
        preIdx = 0
        return helper(0, len(inorder))

    def buildTree(self, preorder, inorder, preorderStart=0, preorderEnd=None, inorderStart=0, inorderEnd=None):
        if preorderEnd is None:
            preorderEnd = len(preorder) - 1

        if inorderEnd is None:
            inorderEnd = len(inorder) - 1

        if preorderStart > len(preorder) - 1 or inorderStart > inorderEnd:
            return None

        rootValue = preorder[preorderStart]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(
            preorder, inorder, preorderStart+1, inorderIndex, inorderStart, inorderIndex-1)
        root.right = self.buildTree(preorder, inorder, preorderStart +
                                    inorderIndex+1-inorderStart, preorderEnd, inorderIndex+1, inorderEnd)

        return root

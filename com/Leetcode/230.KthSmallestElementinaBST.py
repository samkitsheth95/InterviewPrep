# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallestRecursive(self, root: TreeNode, k: int) -> int:
        ans = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans[k - 1]

    def kthSmallestIterative(self, root: TreeNode, k: int) -> int:
        ans, stack, curr = [], [], root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right
        return ans[k - 1]

    def kthSmallestIterativeUptoK(self, root: TreeNode, k: int) -> int:
        ans, stack, curr = [], [], root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                k -= 1
                if not k:
                    return curr.val
                curr = curr.right
        return ans[k - 1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBSTRecursiveNaive(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        ans = 0
        if low <= root.val <= high:
            ans += root.val
        return ans + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

    def rangeSumBSTIterative(self, root: TreeNode, low: int, high: int) -> int:
        stack, ans = [root], 0
        while stack:
            current = stack.pop()
            if current:
                if low <= current.val <= high:
                    ans += current.val
                if low < current.val:
                    stack.append(current.left)
                if current.val < high:
                    stack.append(current.right)
        return ans

    def rangeSumBSTRecursiveTwo(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

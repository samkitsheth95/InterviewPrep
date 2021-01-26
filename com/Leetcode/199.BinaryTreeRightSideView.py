from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def rightSideViewRecursive(self, root: TreeNode) -> List[int]:
        ans = []

        def helper(root, depth):
            if not root:
                return
            if depth == len(ans):
                ans.append(root.val)
            helper(root.right, depth + 1)
            helper(root.left, depth + 1)
        helper(root, 0)

        return ans

    def rightSideViewIterative(self, root: TreeNode) -> List[int]:
        if not root:
            return
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(curr.val)
        return ans

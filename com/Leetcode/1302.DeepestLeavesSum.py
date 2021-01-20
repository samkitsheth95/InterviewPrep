from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def deepestLeavesSumDFS(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        ans = 0
        deepestDepth = 0
        while stack:
            curr, depth = stack.pop()
            if curr.left or curr.right:
                if curr.left:
                    stack.append((curr.left, depth + 1))
                if curr.right:
                    stack.append((curr.right, depth + 1))
            else:
                if depth > deepestDepth:
                    deepestDepth = depth
                    ans = curr.val
                elif depth == deepestDepth:
                    ans += curr.val
        return ans
    
    def deepestLeavesSumBFS(self, root: TreeNode) -> int:
        q = deque([root])
        while q:
            size = len(q)
            ans = 0
            for i in range(size):
                curr = q.popleft()
                ans += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans
from collections import deque
import sys
sys.path.append('com/DataStructure/Python')
from BinarySearchTree import BinarySearchTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invertTreeBfs(self, root):
        q = deque()
        q.append(root)
        while q:
            current = q.popleft()
            if current:
                current.left, current.right = current.right, current.left
                q.append(current.left)
                q.append(current.right)
        return root

    def invertTreeDfs(self, root):
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                current.left, current.right = current.right, current.left
                stack.append(current.left)
                stack.append(current.right)
        return root

    def invertTreeRecursion(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTreeRecursion(root.left)
        self.invertTreeRecursion(root.right)
        return root


test = BinarySearchTree()
test.addNode(4)
test.addNode(2)
test.addNode(7)
test.addNode(1)
test.addNode(3)
test.addNode(6)
test.addNode(9)
test.printTreeBfs(test.getRoot())
sol = Solution()
test.printTreeBfs(sol.invertTreeRecursion(test.getRoot()))

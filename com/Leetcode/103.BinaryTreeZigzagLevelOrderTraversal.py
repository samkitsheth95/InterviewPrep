# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        lvl = 1
        q = deque()
        q.append(root)
        while q:
            qsize = len(q)
            levelElements = []
            if lvl % 2 == 0:
                while qsize > 0:
                    current = q.pop()
                    levelElements.append(current.val)
                    if current.right:
                        q.appendleft(current.right)
                    if current.left:
                        q.appendleft(current.left)
                    qsize -= 1
            if lvl % 2 != 0:
                while qsize > 0:
                    current = q.popleft()
                    levelElements.append(current.val)
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)
                    qsize -= 1
            ans.append(levelElements)
            lvl += 1
        return ans

    def zigzagLevelOrderNaive(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        lvl = 1
        q = deque()
        q.append(root)
        while q:
            qsize = len(q)
            levelElements = []
            while qsize > 0:
                current = q.popleft()
                levelElements.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                qsize -= 1
            if lvl % 2 == 0:
                levelElements.reverse()
                ans.append(levelElements)
            else:
                ans.append(levelElements)
            lvl += 1
        return ans

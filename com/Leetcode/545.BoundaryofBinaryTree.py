# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getLeftView(self, root, ans):
        while root:
            if not root.left and not root.right:
                return
            ans.append(root.val)
            if root.left:
                root = root.left
            else:
                root = root.right

    def getChild(self, root, ans):
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                ans.append(curr.val)
                continue
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def getRightView(self, root, ans):
        temp = []
        while root:
            if not root.left and not root.right:
                break
            temp.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        temp.reverse()
        ans.extend(temp)

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        self.getLeftView(root.left, ans)
        self.getChild(root.left, ans)
        self.getChild(root.right, ans)
        self.getRightView(root.right, ans)
        return ans

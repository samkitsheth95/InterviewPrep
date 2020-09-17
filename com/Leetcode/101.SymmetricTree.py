class Solution:

    def sym(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        else:
            return left.val == right.val and self.sym(left.left, right.right) and self.sym(left.right, right.left)

    def isSymmetric(self, root):
        if not root:
            return True
        return self.sym(root.left, root.right)

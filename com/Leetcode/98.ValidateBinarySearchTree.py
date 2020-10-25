import sys
sys.path.append('com/DataStructure/Python')
from BinarySearchTree import BinarySearchTree


class Solution:
    def isValidTree(self, root, minN, maxN):
        if root is None:
            return True
        if root.val > minN and root.val < maxN:
            return self.isValidTree(root.left, minN, root.val) and self.isValidTree(root.right, root.val, maxN)
        else:
            return False

    def isValidBST(self, root):
        return self.isValidTree(root, float('-inf'), float('inf'))


test = BinarySearchTree()
test.addNode(6)
test.addNode(4)
test.addNode(8)
test.printTree(test.getRoot())
sol = Solution()
print(sol.isValidBST(test.getRoot()))

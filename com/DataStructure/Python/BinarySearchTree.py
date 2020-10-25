from collections import deque


class TreeNode:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addNode(self, val):
        newNode = TreeNode(val)
        fNode = self.root
        while True:
            if not self.root:
                self.root = newNode
                break
            elif val <= fNode.val:
                if not fNode.left:
                    fNode.left = newNode
                    break
                else:
                    fNode = fNode.left
            else:
                if not fNode.right:
                    fNode.right = newNode
                    break
                else:
                    fNode = fNode.right

    def printTree(self, fNode):
        if fNode:
            print(fNode.val, end=" ")
            self.printTree(fNode.left)
            self.printTree(fNode.right)

    def printTreeBfs(self, fNode):
        q = deque()
        q.append(fNode)
        while q:
            current = q.popleft()
            if current:
                print(current.val, end=" ")
                q.append(current.left)
                q.append(current.right)
        print()


if __name__ == "__main__":
    newBinaryTree = BinarySearchTree()
    newBinaryTree.addNode(10)
    newBinaryTree.addNode(15)
    newBinaryTree.addNode(19)
    newBinaryTree.addNode(17)
    newBinaryTree.addNode(11)
    newBinaryTree.printTreeBfs(newBinaryTree.root)

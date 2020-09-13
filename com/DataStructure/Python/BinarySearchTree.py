class Node:

    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def addNode(self, val):
        newNode = Node(val)
        fNode = self.root
        while True:
            if self.root == None:
                self.root = newNode
                break
            elif val <= fNode.val:
                if fNode.left == None:
                    fNode.left = newNode
                    break
                else:
                    fNode = fNode.left
            else:
                if fNode.right == None:
                    fNode.right = newNode
                    break
                else:
                    fNode = fNode.right
    
    def printTree(self,fNode):
        if fNode != None:
            print(fNode.val, end = " ")
            self.printTree(fNode.left)
            self.printTree(fNode.right)

    
if __name__ == "__main__":
    newBinaryTree = BinarySearchTree()
    newBinaryTree.addNode(10)
    newBinaryTree.addNode(15)
    newBinaryTree.addNode(19)
    newBinaryTree.addNode(17)
    newBinaryTree.addNode(11)
    newBinaryTree.printTree(newBinaryTree.root)
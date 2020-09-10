class Node:

    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def addNode(self, data):
        newNode = Node(data)
        fNode = self.root
        while True:
            if self.root == None:
                self.root = newNode
                break
            elif data <= fNode.data:
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
            print(fNode.data, end = " ")
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
class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.a = {}
        self.space = capacity
        self.start = Node()
        self.end = Node()

    def get(self, key: int) -> int:
        if key in self.a:
            node = self.a[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if len(self.a) < self.space or key in self.a:
            if key in self.a:
                self.remove(self.a[key])
                self.a[key] = newNode
                self.add(newNode)
            else:
                self.a[key] = newNode
                self.add(newNode)
        else:
            lruKey = self.removeLRU()
            del self.a[lruKey]
            self.a[key] = newNode
            self.add(newNode)

    def add(self, newNode):
        if not self.end.prev:
            self.end.prev = newNode
            self.start.next = newNode
        else:
            newNode.prev = self.end.prev
            self.end.prev.next = newNode
            self.end.prev = newNode

    def removeLRU(self):
        key = self.start.next.key
        if not self.start.next.next:
            self.start.next = None
            self.end.prev = None
        else:
            self.start.next.next.prev = None
            self.start.next = self.start.next.next
        return key

    def remove(self, node):
        if not node.prev and not node.next:
            self.start.next = None
            self.end.prev = None
        elif not node.prev:
            self.start.next = node.next
            node.next.prev = None
        elif not node.next:
            self.end.prev = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def printLL(self, j):
        current = self.start
        while current.next:
            current = current.next
            print(current.key, end=" ")

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# param_1 = obj.get(key)
# obj.put(key,value)
inputKey = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put",
            "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
inputVal = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [
    4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
obj = LRUCache(inputVal[0][0])
for i in range(1, len(inputVal)):
    if inputKey[i] == "get":
        print(obj.get(inputVal[i][0]), end=" ")
    if inputKey[i] == "put":
        print(obj.put(inputVal[i][0], inputVal[i][1]), end=" ")

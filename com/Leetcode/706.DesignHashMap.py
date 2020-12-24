class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 2069
        self.arr = [[] for _ in range(2069)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        x = self.arr[key % self.mod]
        found = False
        for i in range(len(x)):
            if x[i][0] == key:
                x[i] = (key, value)
                found = True
                break
        if not found:
            x.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        x = self.arr[key % self.mod]
        for kv in x:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        x = self.arr[key % self.mod]
        found = False
        for i in range(len(x)):
            if x[i][0] == key:
                rm = i
                found = True
                break
        if found:
            del x[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

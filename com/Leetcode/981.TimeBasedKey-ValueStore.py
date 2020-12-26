class TimeMap:

    def binarySearch(self, a, key):
        if key < a[0][1]:
            return ''
        elif key >= a[-1][1]:
            return a[-1][0]

        low = 0
        high = len(a) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if a[mid][1] == key:
                return a[mid][0]
            elif a[mid][1] > key:
                high = mid - 1
            else:
                low = mid + 1
        return a[high][0]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        return self.binarySearch(self.d[key], timestamp)

    def getBisect(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None:
            return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

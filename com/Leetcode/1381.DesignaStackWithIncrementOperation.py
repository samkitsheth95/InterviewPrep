# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.addition(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.data = []
        self.addition = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)
            self.addition.append(0)

    def pop(self) -> int:
        if not self.addition:
            return -1
        if len(self.addition) > 1:
            self.addition[-2] += self.addition[-1]
        return self.addition.pop() + self.data.pop()

    def increment(self, k: int, val: int) -> None:
        if self.addition:
            self.addition[min(len(self.addition), k) - 1] += val

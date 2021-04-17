from collections import OrderedDict


class FirstUniqueByMe:

    def __init__(self, nums: List[int]):
        self.funique = OrderedDict()
        self.repeted = set()
        for i in nums:
            if i in self.repeted:
                continue
            elif i in self.funique:
                del self.funique[i]
                self.repeted.add(i)
            else:
                self.funique[i] = True

    def showFirstUnique(self) -> int:
        if len(self.funique):
            for i in self.funique.keys():
                return i
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self.repeted:
            if value in self.funique:
                del self.funique[value]
                self.repeted.add(value)
            else:
                self.funique[value] = True

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freqCount = defaultdict(int)
        self.countstacks = defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.freqCount[x] += 1
        self.countstacks[self.freqCount[x]].append(x)
        if self.freqCount[x] > self.maxfreq:
            self.maxfreq += 1

    def pop(self) -> int:
        removed = self.countstacks[self.maxfreq].pop()
        self.freqCount[removed] -= 1
        if not len(self.countstacks[self.maxfreq]):
            self.maxfreq -= 1
        return removed


operations = ["push", "push", "push", "push",
              "push", "push", "pop", "pop", "pop", "pop"]
values = [[5], [7], [5], [7], [4], [5], [], [], [], []]
freqStack = FreqStack()
for i in range(len(operations)):
    if operations[i] == "push":
        freqStack.push(values[i][0])
    else:
        print(freqStack.pop())

from typing import List


class Solution:

    def correctSeqCompact(self, a, b, value):
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return value[a[i]] < value[b[i]]
        return len(a) <= len(b)

    def correctSeq(self, a, b, value):
        for i in range(min(len(a), len(b))):
            if value[a[i]] == value[b[i]]:
                continue
            elif value[a[i]] < value[b[i]]:
                return True
            else:
                return False
        if len(a) > len(b):
            return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        value = {}
        for index, char in enumerate(order):
            value[char] = index

        for i in range(len(words) - 1):
            if not self.correctSeq(words[i], words[i + 1], value):
                return False

        return True


sol = Solution()
print(sol.isAlienSorted(
    words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))

from typing import List


class Solution:
    def numLen(self, i):
        size = 1
        while i >= 10:
            size += 1
            i = i/10
        return size

    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            if not self.numLen(i) % 2:
                total += 1
        return total


sol = Solution()
print(sol.findNumbers([12, 345, 2, 6, 7896]))

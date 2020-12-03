from typing import List


class Solution:
    def findGold(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        value = max(self.findGold(grid, i + 1, j),
                    self.findGold(grid, i - 1, j),
                    self.findGold(grid, i, j + 1),
                    self.findGold(grid, i, j - 1)) + temp
        grid[i][j] = temp
        return value

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxG = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    tp = self.findGold(grid, i, j)
                    if tp > maxG:
                        maxG = tp
        return maxG


sol = Solution()
print(sol.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))

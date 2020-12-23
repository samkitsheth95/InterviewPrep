from typing import List


class Solution:

    def isValid(self, rows, cols, i, j):
        return 0 <= i < rows and 0 <= j < cols

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    for up, down in directions:
                        if not self.isValid(rows, cols, i + up, j + down) or not grid[i + up][j + down]:
                            ans += 1
        return ans


sol = Solution()
print(sol.islandPerimeter(
    grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))

from typing import List


class Solution:

    def dfs(self, grid: List[List[str]], i: int, j: int, row: int, col: int):
        if not self.isInside(i, j, row, col) or grid[i][j] == '0' or grid[i][j] == '#':
            return 0
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j, row, col)
        self.dfs(grid, i - 1, j, row, col)
        self.dfs(grid, i, j + 1, row, col)
        self.dfs(grid, i, j - 1, row, col)

    def numIslandsRecur(self, grid: List[List[str]]) -> int:
        print(grid)
        ans = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j, row, col)
        return ans

    def isInside(self, i, j, row, col):
        if 0 <= i < row and 0 <= j < col:
            return True
        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        ans = 0
        row, col = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    stack.append([i, j])
                    grid[i][j] = '#'
                    while stack:
                        m, n = stack.pop()
                        for dm, dn in directions:
                            if self.isInside(dm + m, dn + n, row, col) and grid[dm + m][dn + n] == '1':
                                stack.append([dm + m, dn + n])
                                grid[dm + m][dn + n] = '#'
        return ans


sol = Solution()
print(sol.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1"]
]))

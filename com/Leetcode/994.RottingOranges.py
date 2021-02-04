from collections import deque
from typing import List


class Solution:

    def isValid(self, m, n, row, col):
        return 0 <= m < row and 0 <= n < col

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshOrange = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    freshOrange += 1
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q.append([-1, -1])
        ans = -1
        while q:
            m, n = q.popleft()
            if m == -1:
                ans += 1
                if q:
                    q.append([-1, -1])
            else:
                for md, nd in direction:
                    if self.isValid(m + md, n + nd, len(grid), len(grid[0])) and grid[m + md][n + nd] == 1:
                        freshOrange -= 1
                        grid[m + md][n + nd] = 2
                        q.append([m + md, n + nd])
        return ans if freshOrange == 0 else -1

    def dfs(self, grid, i, j, a, k):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == 2 or grid[i][j] == '#':
            return
        temp = grid[i][j]
        grid[i][j] = '#'
        if k < a[i][j] or a[i][j] == 0:
            a[i][j] = k
        self.dfs(grid, i-1, j, a, k+1)
        self.dfs(grid, i+1, j, a, k+1)
        self.dfs(grid, i, j+1, a, k+1)
        self.dfs(grid, i, j-1, a, k+1)
        grid[i][j] = temp

    def orangesRottingRecur(self, grid: List[List[int]]) -> int:
        a = [[0]*len(grid[0]) for _ in range(len(grid))]
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.dfs(grid, i-1, j, a, 1)
                    self.dfs(grid, i+1, j, a, 1)
                    self.dfs(grid, i, j+1, a, 1)
                    self.dfs(grid, i, j-1, a, 1)
        maxL = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and a[i][j] == 0:
                    return -1
                elif maxL < a[i][j]:
                    maxL = a[i][j]
        return maxL


sol = Solution()
print(sol.orangesRottingRecur([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

from typing import List


class Solution:

    def numDistinctIslandsPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1, 'F'), (0, -1, 'B'), (1, 0, 'U'), (-1, 0, 'D')]
        islands = set()

        def isValid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, path, t):
            if not isValid(i, j) or not grid[i][j] or grid[i][j] == -1:
                return ''
            grid[i][j] = -1
            path.append(t)
            for di, dy, mark in directions:
                dfs(i + di, j + dy, path, mark)
            path.append("B")

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, "O")
                    islands.add(str(path))

        return len(islands)

    def numDistinctIslandsFrozen(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        uniqueIslands = set()

        def isValid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, currentIsland, i0, j0):
            if not isValid(i, j) or not grid[i][j] or grid[i][j] == -1:
                return ''
            grid[i][j] = -1
            currentIsland.add(((i - i0), (j - j0)))
            for di, dy in directions:
                dfs(i + di, j + dy, currentIsland, i0, j0)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currentIsland = set()
                    dfs(i, j, currentIsland, i, j)
                    uniqueIslands.add(frozenset(currentIsland))

        return len(uniqueIslands)


sol = Solution()
print(sol.numDistinctIslandsFrozen(
    [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))

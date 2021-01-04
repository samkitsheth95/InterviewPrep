from typing import List
from collections import deque


class Solution:

    def isValid(self, i, j, rows, cols):
        return 0 <= i < rows and 0 <= j < cols

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        pacific, atlantic, ans = set(), set(), []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(matrix, i, j, ocean, prev):
            if not self.isValid(i, j, rows, cols) or ((i, j) in ocean):
                return
            if prev > matrix[i][j]:
                return
            ocean.add((i, j))
            for x, y in directions:
                dfs(matrix, i + x, j + y, ocean, matrix[i][j])

        for k in range(rows):
            dfs(matrix, k, 0, pacific, matrix[k][0])
            dfs(matrix, k, cols - 1, atlantic, matrix[k][cols - 1])

        for k in range(cols):
            dfs(matrix, 0, k, pacific, matrix[0][k])
            dfs(matrix, rows - 1, k, atlantic, matrix[rows - 1][k])

        return list(pacific.intersection(atlantic))

    def dfsNaive(self, matrix, i, j, visited, m, n, prev):
        if not self.isValid(i, j, m, n) or matrix[i][j] == "#" or prev < matrix[i][j]:
            return [0, 0]
        if visited[i][j]:
            return [1, 1]
        setA = [0, 0]
        if i == m - 1 or j == n - 1:
            setA[0] = 1
        if i == 0 or j == 0:
            setA[1] = 1
        temp = matrix[i][j]
        matrix[i][j] = "#"
        c1 = self.dfsNaive(matrix, i + 1, j, visited, m, n, temp)
        c2 = self.dfsNaive(matrix, i, j + 1, visited, m, n, temp)
        c3 = self.dfsNaive(matrix, i - 1, j, visited, m, n, temp)
        c4 = self.dfsNaive(matrix, i, j - 1, visited, m, n, temp)
        if c1[0] or c2[0] or c3[0] or c4[0]:
            setA[0] = 1
        if c1[1] or c2[1] or c3[1] or c4[1]:
            setA[1] = 1
        if setA[0] and setA[1]:
            visited[i][j] = True
        matrix[i][j] = temp
        return setA

    def pacificAtlanticNaive(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    ans.append([i, j])
                    continue
                self.dfsNaive(matrix, i, j, visited, m, n, matrix[i][j])
                if visited[i][j]:
                    ans.append([i, j])
        return ans

    def pacificAtlanticQueue(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        pacific, atlantic, ans = set(), set(), []
        pacificQueue, atlanticQueue = deque(), deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(matrix, q, ocean):
            while q:
                i, j = q.popleft()
                ocean.add((i, j))
                for x, y in directions:
                    if self.isValid(i + x, j + y, rows, cols) and ((i + x, j + y) not in ocean) and matrix[i][j] <= matrix[i + x][j + y]:
                        q.append((i + x, j + y))

        for k in range(rows):
            pacificQueue.append((k, 0))
            atlanticQueue.append((k, cols - 1))

        for k in range(cols):
            pacificQueue.append((0, k))
            atlanticQueue.append((rows - 1, k))

        bfs(matrix, pacificQueue, pacific)
        bfs(matrix, atlanticQueue, atlantic)

        return list(pacific.intersection(atlantic))


sol = Solution()
print(sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
      2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

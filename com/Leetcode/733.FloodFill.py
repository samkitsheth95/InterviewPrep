from typing import List
from collections import deque


class Solution:

    def isValidI(self, i, j, rows, cols):
        return 0 <= i < rows and 0 <= j < cols

    def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(image), len(image[0])
        q = deque()
        q.append((sr, sc))

        while q:
            i, j = q.popleft()
            image[i][j] = newColor
            for x, y in directions:
                if self.isValidI(i + x, j + y, rows, cols) and image[i + x][j + y] == oldColor:
                    q.append((i + x, j + y))
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(image), len(image[0])

        def isValid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(x, y):
            if isValid(x, y) and image[x][y] == oldColor:
                image[x][y] = newColor
                for nx, ny in directions:
                    dfs(x + nx, y + ny)

        dfs(sr, sc)
        return image


sol = Solution()
print(sol.floodFillBFS(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                       sr=1, sc=1, newColor=2))

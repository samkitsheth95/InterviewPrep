from typing import List
from collections import deque


class Solution:

    # Right Way To solve
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if not rooms[i][j]:
                    q.append([i, j])

        def isValid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def bfs(q, depth=0):
            while q:
                depth += 1
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for ix, jy in direction:
                        if isValid(i + ix, j + jy) and rooms[i + ix][j + jy] == 2147483647:
                            q.append([i + ix, j + jy])
                            rooms[i + ix][j + jy] = depth

        bfs(q)

    # Wrong Way To Solve
    # Why??
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if not rooms[i][j]:
                    q.append([i, j])

        def isValid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def bfs(q, depth=0):
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for ix, jy in direction:
                        if isValid(i + ix, j + jy) and rooms[i + ix][j + jy] == 2147483647:
                            q.append([i + ix, j + jy])
                    # should not do the next line
                    # Why?
                    rooms[i][j] = min(rooms[i][j], depth)
                depth += 1
        bfs(q)


sol = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647,
                                           2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
sol.wallsAndGates(rooms)
print(rooms)

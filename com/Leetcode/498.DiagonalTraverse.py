from typing import List


class Solution:
    def dfs(self, matrix, i, j, k):
        diag = []
        while i >= 0 and j < len(matrix[0]):
            diag.append(matrix[i][j])
            i -= 1
            j += 1
        if k % 2:
            diag.reverse()
        return diag

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        k = 0

        for i in range(len(matrix)):
            ans.extend(self.dfs(matrix, i, 0, k))
            k += 1

        for i in range(1, len(matrix[0])):
            ans.extend(self.dfs(matrix, len(matrix) - 1, i, k))
            k += 1

        return ans


sol = Solution()
print(sol.findDiagonalOrder(matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

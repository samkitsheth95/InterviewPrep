from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mx, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i]
                                   [j - 1], dp[i - 1][j]) + 1
                    mx = max(mx, dp[i][j])
                else:
                    dp[i][j] = 0
        return mx ** 2

    def maximalSquareOptimized(self, matrix: List[List[str]]) -> int:
        mx, prev, m, n = 0, 0, len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    mx = max(mx, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return mx ** 2


sol = Solution()
print(sol.maximalSquareOptimized(matrix=[["1", "0", "1", "0", "0"], [
      "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))

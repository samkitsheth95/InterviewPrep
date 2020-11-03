from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]

    def uniquePathsSpace(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]

    # In other words, we're asked to compute in how many ways one could choose pp elements from p + kp+k elements.
    # In mathematics, that's called binomial coefficients
    def uniquePathsMath(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)


sol = Solution()
print(sol.uniquePathsMath(3, 2))

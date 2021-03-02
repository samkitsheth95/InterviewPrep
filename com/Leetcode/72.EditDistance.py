class Solution:

    def backtrace(self, word1, word2, dp):
        m, n = len(word2), len(word1)
        while m > 0 and n > 0:
            if word1[n - 1] == word2[m - 1]:
                m -= 1
                n -= 1
            elif (dp[m][n] - 1) == dp[m][n - 1]:
                print("word Delete", word1[n - 1])
                n -= 1
            elif (dp[m][n] - 1) == dp[m - 1][n]:
                print("Word Inserted", word2[m - 1])
                m -= 1
            else:
                print("Word Replaced", word1[n - 1], word2[m - 1])
                m -= 1
                n -= 1

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                                   [j], dp[i][j - 1]) + 1
        self.backtrace(word1, word2, dp)
        return dp[-1][-1]

    def minDistanceSpace(self, word1: str, word2: str) -> int:
        dp, prev = [i for i in range((len(word2)+1))], 0
        for i in range(1, len(word1) + 1):
            for j in range(len(word2) + 1):
                nex_prev = dp[j]
                if j == 0:
                    dp[j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(prev, dp[j-1], dp[j]) + 1
                prev = nex_prev
        return dp[-1]


sol = Solution()
print(sol.minDistanceSpace(word1="horse", word2="ros"))

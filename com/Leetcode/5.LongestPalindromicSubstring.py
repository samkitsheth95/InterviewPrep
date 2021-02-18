from operator import itemgetter


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, ans = len(s), ""
        for i in range(n):
            a = self.helper(s, i, i)
            b = self.helper(s, i, i + 1)
            ans = max([a, b, ans], key=len)
        return ans

    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j]

    def longestPalindromedp(self, s: str) -> str:
        n, ans = len(s), (0, 0, 0)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            k = 0
            for j in range(i, n):
                if k == j:
                    dp[k][j] = True
                elif j - k == 1 and s[k] == s[j]:
                    dp[k][j] = True
                elif s[k] == s[j] and dp[k + 1][j - 1]:
                    dp[k][j] = True
                if dp[k][j] and j - k + 1 >= ans[0]:
                    ans = (j - k + 1, k, j + 1)
                k += 1
        return s[ans[1]:ans[2]]

    def longestPalindromeNoSubstring(self, s: str) -> str:
        n, ans = len(s), (0, 0, 0)
        for i in range(n):
            a = self.helperSub(s, i, i)
            b = self.helperSub(s, i, i + 1)
            ans = max([a, b, ans], key=itemgetter(0))
        return s[ans[1]:ans[2]]

    def helperSub(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (j - i - 1, i + 1, j)


sol = Solution()
print(sol.longestPalindromeNoSubstring(s="babad"))

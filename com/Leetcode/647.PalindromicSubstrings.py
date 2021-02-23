class Solution:
    def countSubstringsdp(self, s: str) -> int:
        n, ans = len(s), 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            k = 0
            for j in range(i, n):
                if k == j:
                    dp[k][j] = True
                    ans += 1
                elif j - k == 1 and s[k] == s[j]:
                    dp[k][j] = True
                    ans += 1
                elif s[k] == s[j] and dp[k + 1][j - 1]:
                    dp[k][j] = True
                    ans += 1
                k += 1
        return ans

    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            ans += self.helper(s, i, i)
            ans += self.helper(s, i, i + 1)
        return ans

    def helper(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            count += 1
        return count


sol = Solution()
print(sol.countSubstringsdp("aaa"))

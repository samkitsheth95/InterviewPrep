class Solution:
    def maxDepth(self, s: str) -> int:
        ans, openBracket = 0, 0
        for i in s:
            if i == '(':
                openBracket += 1
                ans = max(ans, openBracket)
            elif i == ')':
                openBracket -= 1
        return ans


sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))

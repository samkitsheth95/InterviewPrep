class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        step = 0
        while y > x:
            if y % 2:
                y += 1
            else:
                y = y // 2
            step += 1
        return step + (x - y)


sol = Solution()
print(sol.brokenCalc(x=3, y=10))

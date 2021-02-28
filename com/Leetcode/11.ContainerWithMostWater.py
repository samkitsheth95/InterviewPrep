from typing import List


class Solution:

    def maxAreaNaive(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                ans = max(ans, (j - i) * min(height[i], height[j]))
        return ans

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            if height[i] > height[j]:
                ans = max(ans, (j - i) * height[j])
                j -= 1
            else:
                ans = max(ans, (j - i) * height[i])
                i += 1
        return ans


sol = Solution()
print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))

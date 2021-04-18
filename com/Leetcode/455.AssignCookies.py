from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


sol = Solution()
print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))

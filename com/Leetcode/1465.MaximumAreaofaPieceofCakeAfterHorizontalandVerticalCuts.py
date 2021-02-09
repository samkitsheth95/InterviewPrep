from typing import List


class Solution:

    def maxAreaRock(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        H, V = max(horizontalCuts[0], h - horizontalCuts[-1]
                   ), max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            H = max(H, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            V = max(V, verticalCuts[i] - verticalCuts[i - 1])
        return H * V % 1000000007

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hmax, vmax, prev = 0, 0, 0
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in horizontalCuts:
            hmax = max(hmax, i - prev)
            prev = i
        hmax = max(hmax, h - horizontalCuts[-1])
        prev = 0
        for i in verticalCuts:
            vmax = max(vmax, i - prev)
            prev = i
        vmax = max(vmax, w - verticalCuts[-1])
        return (hmax * vmax) % (10**9 + 7)


sol = Solution()
print(sol.maxAreaRock(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))

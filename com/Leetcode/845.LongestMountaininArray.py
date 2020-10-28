from typing import List


class Solution:
    def longestMountain(self, a: List[int]) -> int:
        n = len(a)
        i = ans = 0
        while i < n:
            if i + 1 < n and a[i] < a[i + 1]:
                k = 0
                while i + 1 < n and a[i] < a[i + 1]:
                    i += 1
                    k += 1
                if i + 1 < n and a[i] > a[i + 1]:
                    while i + 1 < n and a[i] > a[i + 1]:
                        i += 1
                        k += 1
                    ans = max(ans, k + 1)
            else:
                i += 1
        return ans


sol = Solution()
print(sol.longestMountain([2, 1, 4, 7, 3, 2, 5]))

from typing import List
from math import ceil


class Solution:

    def compute_sum(self, x, nums):
        return sum([ceil(n / x) for n in nums])

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = 1
        left, right = 1, max(nums)
        while left <= right:
            pivot = (right + left) >> 1
            num = self.compute_sum(pivot, nums)
            if num <= threshold:
                ans = pivot
                right = pivot - 1
            else:
                left = pivot + 1
        return ans


sol = Solution()
print(sol.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))

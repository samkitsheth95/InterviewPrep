from typing import List
from bisect import bisect_left, bisect_right


class Solution:

    def customBinary(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        firstIndex = n
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                firstIndex = mid
                high = mid - 1
            else:
                low = mid + 1
        return firstIndex

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = self.customBinary(nums, target)
        b = self.customBinary(nums, target + 1)
        if a != len(nums) and nums[a] == target:
            return [a, b-1]
        else:
            return [-1, -1]

    def searchRangeLib(self, nums: List[int], target: int) -> List[int]:
        a = bisect_left(nums, target)
        b = bisect_right(nums, target)

        if a != len(nums) and nums[a] == target:
            return [a, b-1]
        else:
            return [-1, -1]


sol = Solution()
print(sol.searchRangeLib(nums=[5, 7, 7, 8, 8, 10], target=8))

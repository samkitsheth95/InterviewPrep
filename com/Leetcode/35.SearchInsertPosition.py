from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        insertPosition = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                insertPosition = mid
                high = mid - 1
            else:
                low = mid + 1
        return insertPosition


sol = Solution()
print(sol.searchInsert(nums=[1, 3, 5, 6], target=5))

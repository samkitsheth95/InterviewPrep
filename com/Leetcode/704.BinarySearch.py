from typing import List


class Solution:
    def recur(self, low, high, nums, target):
        if low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            return self.recur(low, high, nums, target)
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def searchRec(self, nums: List[int], target: int) -> int:
        return self.recur(0, len(nums) - 1, nums, target)


sol = Solution()
print(sol.searchRec(nums=[-1, 0, 3, 5, 9, 12], target=9))

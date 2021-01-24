from typing import List
from random import randint


class Solution:

    def findPivot(self, nums, low, high):
        pivotLoc = randint(low, high)
        pivot = nums[pivotLoc]
        nums[low], nums[pivotLoc] = nums[pivotLoc], nums[low]
        pivotLoc = low
        low += 1
        while low <= high:
            while low <= high and nums[low] <= pivot:
                low += 1
            while low <= high and nums[high] > pivot:
                high -= 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
        nums[high], nums[pivotLoc] = nums[pivotLoc], nums[high]
        return high

    def quicksort(self, nums, low, high):
        if low < high:
            pivot = self.findPivot(nums, low, high)
            self.quicksort(nums, low, pivot - 1)
            self.quicksort(nums, pivot + 1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums


sol = Solution()
print(sol.sortArray(nums=[5, 2, 3, 1]))

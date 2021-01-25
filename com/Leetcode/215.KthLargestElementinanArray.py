from typing import List
from collections import Counter
from random import randint
import heapq


class Solution:

    def findPivot(self, nums, low, high):
        pivotLoc = randint(low, high)
        pivot = nums[pivotLoc]
        nums[low], nums[pivotLoc] = nums[pivotLoc], nums[low]
        pivotLoc = low
        low += 1
        while low <= high:
            while low <= high and nums[low] > pivot:
                low += 1
            while low <= high and nums[high] <= pivot:
                high -= 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
        nums[high], nums[pivotLoc] = nums[pivotLoc], nums[high]
        return high

    def quickselect(self, nums, low, high, k):
        if low <= high:
            pivot = self.findPivot(nums, low, high)
            if pivot == k:
                return nums[pivot]
            elif pivot > k:
                return self.quickselect(nums, low, pivot - 1, k)
            else:
                return self.quickselect(nums, pivot + 1, high, k)

    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = Counter(nums).items()
        data = sorted(freq, key=lambda x: -x[0])
        for key, frequency in data:
            k -= frequency
            if k <= 0:
                return key

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


sol = Solution()
print(sol.findKthLargestQuickSelect(nums=[3, 2, 1, 5, 6, 4], k=2))

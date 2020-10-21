class Solution:
    
    def findPivot(self, nums):
        low = 0
        high = len(nums) - 1
        if (nums[low] < nums[high]):
            return 0;
        while(low <= high):
            mid = (low + high) // 2            
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    def binSearch(self, nums, target, low, high):        
        while(low <= high):
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        pivot = self.findPivot(nums)
        if pivot == 0:
            return self.binSearch(nums, target, 0, n - 1)
        if target < nums[0]:
            return self.binSearch(nums, target, pivot, n - 1)
        return self.binSearch(nums, target, 0, pivot)
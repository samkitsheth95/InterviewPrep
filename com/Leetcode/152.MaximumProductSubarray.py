from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxAll = nums[0]
        maxRunning = nums[0]
        minRunning = nums[0]
        for i in range(1, len(nums)):
            tmp = maxRunning
            maxRunning = max(nums[i], minRunning *
                             nums[i], maxRunning * nums[i])
            minRunning = min(nums[i], minRunning * nums[i], tmp * nums[i])
            maxAll = max(maxAll, maxRunning)
        return maxAll


sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))

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

    def maxProduct1(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far


sol = Solution()
print(sol.maxProduct1([2, 3, -2, 4]))

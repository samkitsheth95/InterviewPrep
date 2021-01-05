from typing import List


class Solution:

    def canJumpGreedyTwo(self, nums: List[int]) -> bool:
        maxReach, i = 0, 0
        while i < len(nums) and i <= maxReach:
            maxReach = max(maxReach, i+nums[i])
            i += 1
        return i == len(nums)

    def canJumpGreedyOne(self, nums: List[int]) -> bool:
        i, j = 0, 0
        while j < len(nums) - 1 and i <= j:
            j = max(j, i + nums[i])
            if 1 + i <= j:
                i += 1
            if i == j and nums[i] == 0:
                break
        if j >= len(nums) - 1:
            return True
        else:
            return False

    def canJumpGreedyEasy(self, nums: List[int]) -> bool:
        n, maxReach, i = len(nums) - 1, 0, 0
        while i <= maxReach:
            maxReach = max(maxReach, i + nums[i])
            i += 1
            if maxReach >= n:
                return True
        return False


sol = Solution()
print(sol.canJumpGreedyTwo(nums=[2, 3, 1, 1, 4]))

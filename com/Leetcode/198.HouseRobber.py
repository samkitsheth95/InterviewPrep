from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, now = 0, 0
        for i in nums:
            temp = prev
            prev = now
            now = max(prev, temp + i)
        return now


sol = Solution()
print(sol.rob(nums=[1, 2, 3, 1]))

from typing import List


class Solution:

    def firstMissingPositiveNaive(self, nums: List[int]) -> int:
        nums.sort()
        ans  = 1
        for i in nums:
            if i == ans:
                ans += 1
        return ans

    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            val = abs(nums[i])
            if val == n:
                if nums[0] > 0:
                    nums[0] = -nums[0]
            elif nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(1, n):
            if nums[i] > 0:
                return i
        return n + 1 if nums[0] < 0 else n


sol = Solution()
print(sol.firstMissingPositive(nums=[1, 2, 0]))

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans


sol = Solution()
print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

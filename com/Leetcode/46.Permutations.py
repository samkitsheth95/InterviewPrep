from typing import List


class Solution:

    def helper(self, nums, lvl, ans):
        if lvl == len(nums) - 1:
            ans.append(nums[:])
        else:
            for i in range(lvl, len(nums)):
                nums[lvl], nums[i] = nums[i], nums[lvl]
                self.helper(nums, lvl + 1, ans)
                nums[lvl], nums[i] = nums[i], nums[lvl]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, 0, ans)
        return ans


sol = Solution()
print(sol.permute(nums=[1, 2, 3]))

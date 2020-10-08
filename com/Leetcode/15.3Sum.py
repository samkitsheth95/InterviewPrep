from typing import List


class Solution:

    def twoSum(self, nums, target, i, ans) -> List[int]:
        low = i + 1
        high = len(nums) - 1
        while low < high:
            currentSum = nums[low] + nums[high]
            if currentSum == target:
                ans.append((-target, nums[low], nums[high]))
                low += 1
                high -= 1
                while low < high and nums[low-1] == nums[low]:
                    low += 1
                while low < high and nums[high] == nums[high+1]:
                    high -= 1
            elif currentSum > target:
                high -= 1
            else:
                low += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, -nums[i], i, ans)
        return ans


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))

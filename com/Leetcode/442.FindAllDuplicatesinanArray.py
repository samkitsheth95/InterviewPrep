from typing import List


class Solution:

    def findDuplicatesSort(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans

    def findDuplicatesSet(self, nums: List[int]) -> List[int]:
        values = set()
        ans = []
        for i in nums:
            if i in values:
                ans.append(i)
            else:
                values.add(i)
        return ans

    # no hashset or sort. O(1) Space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            x = abs(i) - 1
            if nums[x] < 0:
                ans.append(abs(i))
            else:
                nums[x] *= -1
        return ans


sol = Solution()
print(sol.findDuplicatesSort([4, 3, 2, 7, 8, 2, 3, 1]))

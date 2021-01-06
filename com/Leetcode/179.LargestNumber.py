from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:

    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

    def compare(self, x, y):
        return str(x) + str(y) >= str(y) + str(x)

    def comparer(self, x, y):
        return str(x) + str(y) < str(y) + str(x)

    def pivot(self, nums, left, right):
        L, R = left, right
        p = nums[left]
        while left < right:
            while left < len(nums) - 1 and self.compare(nums[left], p):
                left += 1
            while right >= 0 and self.comparer(nums[right], p):
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[L], nums[right] = nums[right], nums[L]
        return right

    def quicksort(self, nums, left, right):
        if left < right:
            pivot = self.pivot(nums, left, right)
            self.quicksort(nums, left, pivot - 1)
            self.quicksort(nums, pivot + 1, right)

    def largestNumberQuicksort(self, nums: List[int]) -> str:
        self.quicksort(nums, 0, len(nums) - 1)
        return "0" if not nums[0] else str(''.join(map(str, nums)))


sol = Solution()
print(sol.largestNumberQuicksort(nums=[3, 30, 34, 5, 9]))

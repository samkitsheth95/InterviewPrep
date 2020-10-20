class Solution:

    def custReverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        self.custReverse(nums, 0, k - 1)
        self.custReverse(nums, k, n - 1)


sol = Solution()
print(sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        j, total, pairs = 0, 1, 0
        for i in range(len(nums)):
            if nums[i] > k:
                j = i + 1
                total = 1
            else:
                pairs += 1
                total *= nums[i]
                while total >= k and j <= i:
                    total //= nums[j]
                    j += 1
                pairs += i - j
        return pairs
    
    def numSubarrayProductLessThanKSolution(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


prob = Solution()
print(prob.numSubarrayProductLessThanK([10, 5, 2, 4], 1000))

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        runningTotal, ans = 0, 0
        count[0] = 1
        for num in nums:
            runningTotal += num
            if runningTotal - k in count:
                ans += count[runningTotal - k]
            count[runningTotal] += 1
        return ans


sol = Solution()
print(sol.subarraySum(nums=[1, 1, 1], k=2))

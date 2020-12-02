from collections import Counter
from typing import List


class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        for i in freq:
            if k and i + k in freq or not k and freq[i] > 1:
                ans += 1
        return ans


sol = Solution()
print(sol.findPairs(nums=[3, 1, 4, 1, 5], k=2))

from typing import List
from collections import Counter
import heapq


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = Counter(nums).items()
        data = sorted(freq, key=lambda x: -x[0])
        for key, frequency in data:
            k -= frequency
            if k <= 0:
                return key

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


sol = Solution()
print(sol.findKthLargestHeap(nums=[3, 2, 1, 5, 6, 4], k=2))

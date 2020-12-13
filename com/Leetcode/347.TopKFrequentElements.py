from typing import List
from collections import Counter
import heapq


class Solution:

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).items()
        bucket = [[] for _ in range(len(nums) + 1)]
        for value, frequency in count:
            bucket[frequency].append(value)
        flatBucket = [item for sublist in bucket for item in sublist]
        flatBucket.reverse()
        return flatBucket[:k]

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums).most_common()
        ans = []
        for i in range(k):
            ans.append(freq[i][0])
        return ans


sol = Solution()
print(sol.topKFrequentBucket(nums=[1, 1, 1, 2, 2, 3], k=2))

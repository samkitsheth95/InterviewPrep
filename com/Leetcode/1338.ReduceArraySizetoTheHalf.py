from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freq = freq.most_common()
        numRequired = len(arr) // 2
        start = 0
        while numRequired > 0:
            numRequired -= freq[start][1]
            start += 1
        return start


sol = Solution()
print(sol.minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))

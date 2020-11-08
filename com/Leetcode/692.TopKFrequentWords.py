from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        ans = []
        for key, value in frequency.items():
            ans.append([key, value])
        ans.sort(key=lambda x: (-x[1], x[0]))
        return [ans[i][0] for i in range(k)]


sol = Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))

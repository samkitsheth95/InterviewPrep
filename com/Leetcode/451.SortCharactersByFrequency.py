from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq.most_common()
        ans = ""
        for i in freq.most_common():
            ans += i[0] * i[1]
        return ans


sol = Solution()
print(sol.frequencySort("tree"))

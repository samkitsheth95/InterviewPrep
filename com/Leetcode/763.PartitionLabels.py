from typing import List


class Solution:

    def partitionLabelsLeetcode(self, s):
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

    def partitionLabels(self, s: str) -> List[int]:
        lastLocation = [0] * 26
        for i, c in enumerate(s):
            lastLocation[ord(c) - ord('a')] = i
        ans = []
        i, j, start = 0, 0, 0
        while i < len(s):
            if lastLocation[ord(s[i]) - ord('a')] > j:
                j = lastLocation[ord(s[i]) - ord('a')]
            if i == j:
                ans.append(j - start + 1)
                start = i + 1
            i += 1
        return ans


sol = Solution()
print(sol.partitionLabelsLeetcode(s="ababcbacadefegdehijhklij"))

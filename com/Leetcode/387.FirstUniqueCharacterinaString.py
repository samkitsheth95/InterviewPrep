from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [[0, 0] for i in range(26)]
        gMin = len(s)
        for i in range(len(s)):
            temp = ord(s[i]) - ord('a')
            freq[temp][0] += 1
            freq[temp][1] = i

        for i in range(len(freq)):
            if freq[i][0] == 1 and freq[i][1] < gMin:
                gMin = freq[i][1]

        return -1 if gMin == len(s) else gMin

    def firstUniqCharCounter(self, s: str) -> int:
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


sol = Solution()
print(sol.firstUniqCharCounter("leetcode"))

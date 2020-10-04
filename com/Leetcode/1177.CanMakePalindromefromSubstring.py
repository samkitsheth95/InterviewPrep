from typing import List


class Solution:

    def isValid(self, s, q):
        hashMap = [0] * 26
        start = q[0]
        end = q[1]
        lengthOfS = end - start + 1
        k = (q[2] + 1 if lengthOfS % 2 else q[2]) * 2
        while start <= end:
            hashMap[ord(s[start]) - 97] += 1
            start += 1
        change = 0
        for i in range(26):
            if hashMap[i] % 2 != 0:
                change += 1
            if k - change < 0:
                return False
        return True

    def canMakePaliQueriesNaive(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        for query in queries:
            ans.append(self.isValid(s, query))
        return ans

    def canMakePaliQueriesOne(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord('a')] += 1
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]

    def canMakePaliQueriesTwo(self, s: str, queries: List[List[int]]) -> List[bool]:
        odds = [[False] * 26]
        for i, c in enumerate(s):
            odds.append(odds[i][:])
            odds[i + 1][ord(c) - ord('a')] ^= True
        return [sum(odds[hi + 1][i] ^ odds[lo][i] for i in range(26)) // 2 <= k for lo, hi, k in queries]

    def canMakePaliQueriesBest(self, s: str, queries: List[List[int]]) -> List[bool]:
        odds = [False]
        for i, c in enumerate(s):
            odds.append(odds[i] ^ 1 << (ord(c) - ord('a')))
        return [bin(odds[hi + 1] ^ odds[lo]).count('1') // 2 <= k for lo, hi, k in queries]


sol = Solution()
print(sol.canMakePaliQueriesBest(
    "abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))

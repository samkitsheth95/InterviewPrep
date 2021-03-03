from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        freqP, freqS = Counter(p), Counter(s[:len(p)])
        i, j, ans = 0, len(p), []
        while j < len(s):
            if not freqS - freqP:
                ans.append(i)
            freqS[s[i]] -= 1
            freqS[s[j]] += 1
            i += 1
            j += 1
        if not freqS - freqP:
            ans.append(i)
        return ans

    def findAnagramsUsingArray(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        freqP, freqS = [0] * 26, [0] * 26
        for k in p:
            freqP[ord(k) - ord('a')] += 1
        for k in s[:len(p)]:
            freqS[ord(k) - ord('a')] += 1
        i, j, ans = 0, len(p), []
        while j < len(s):
            if freqS == freqP:
                ans.append(i)
            freqS[ord(s[i]) - ord('a')] -= 1
            freqS[ord(s[j]) - ord('a')] += 1
            i += 1
            j += 1
        if freqS == freqP:
            ans.append(i)
        return ans


sol = Solution()
print(sol.findAnagramsUsingArray(s="cbaebabacd", p="abc"))

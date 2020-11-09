from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagramsOrd(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for i in s:
                temp[ord(i) - ord('a')] += 1
            ans[tuple(temp)].append(s)
        return ans.values()


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))

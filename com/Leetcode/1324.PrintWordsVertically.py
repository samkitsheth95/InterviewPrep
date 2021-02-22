from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        ans = ["" for _ in range(len(max(words, key=len)))]
        for idx in range(len(words)):
            j = 0
            for c in words[idx]:
                if len(ans[j]) < idx:
                    ans[j] += " " * (idx - len(ans[j]))
                ans[j] += c
                j += 1
        return ans


sol = Solution()
print(sol.printVertically(s="TO BE OR NOT TO BE"))

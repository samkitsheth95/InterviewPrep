from typing import List


class Solution:

    def makePattern(self, word):
        mapping = {}
        pattern = []
        for char in word:
            pattern.append(mapping.setdefault(char, len(mapping)))
        return pattern

    def findAndReplacePatternSmart(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        matchPattern = self.makePattern(pattern)
        for word in words:
            if self.makePattern(word) == matchPattern:
                ans.append(word)
        return ans

    def findAndReplacePatternShort(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]

    def dosePatternMatch(self, word, pattern):
        mappings = {}
        taken = set()
        for i in range(len(pattern)):
            if pattern[i] in mappings and mappings[pattern[i]] != word[i]:
                return False
            if pattern[i] not in mappings:
                if word[i] in taken:
                    return False
                mappings[pattern[i]] = word[i]
                taken.add(word[i])
        return True

    def findAndReplacePatternNaive(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if self.dosePatternMatch(word, pattern):
                ans.append(word)
        return ans


sol = Solution()
print(sol.findAndReplacePatternSmart(
    words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))

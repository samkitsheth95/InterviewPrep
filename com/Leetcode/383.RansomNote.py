from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = Counter(magazine)
        for i in ransomNote:
            magCount[i] -= 1
            if magCount[i] < 0:
                return False
        return True

    def canConstructShort(self, ransomNote, magazine):
        return not Counter(ransomNote) - Counter(magazine)


sol = Solution()
print(sol.canConstructShort(ransomNote="aa", magazine="aab"))

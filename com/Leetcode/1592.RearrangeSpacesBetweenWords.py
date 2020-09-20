class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = text.split()
        if len(words) == 1:
            spo = text.count(" ")
            thewords = text.split()
            return thewords[0] + " "*spo
        place = " " * (spaces // (len(words)-1))
        extraSpaces = spaces % (len(words)-1)
        ans = ""
        for i in range(len(words)-1):
            ans += words[i] + place
        ans += words[-1]
        return ans + " " * extraSpaces


sol = Solution()
print(sol.reorderSpaces("  this   is  a sentence "))

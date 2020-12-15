class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()
        # sort based on length, this internally uses tim sort which preserves the order when length is same
        words.sort(key=len)
        words[0] = words[0][0].upper() + words[0][1:]
        return ' '.join(words)


sol = Solution()
print(sol.arrangeWords(text="Leetcode is cool"))

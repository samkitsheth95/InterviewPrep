class Solution:

    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')

        def latin(w, i):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)

        return ' '.join(latin(w, i) for i, w in enumerate(S.split()))

    def toGoatLatinNaive(self, S: str) -> str:
        words, ans, i = S.split(), [], 1
        for word in words:
            if word[0] in "aeiouAEIOU":
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += ("a" * i)
            ans.append(word)
            i += 1
        return " ".join(ans)


sol = Solution()
print(sol.toGoatLatinNaive("I speak Goat Latin"))

from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        ans = ['a'] * len(S)
        freq = Counter(S)
        freq = freq.most_common()
        maxLen = len(S) // 2 if not len(S) % 2 else (len(S) // 2) + 1
        if freq[0][1] > maxLen:
            return ""
        start = 0
        temp = freq[start][1]
        for i in range(0, len(S), 2):
            ans[i] = freq[start][0]
            temp -= 1
            if not temp:
                start += 1
                temp = freq[start][1]
        for i in range(1, len(S), 2):
            ans[i] = freq[start][0]
            temp -= 1
            if not temp:
                start += 1
                if start < len(freq):
                    temp = freq[start][1]
                else:
                    break
        return ''.join(ans)


sol = Solution()
print(sol.reorganizeString("aab"))

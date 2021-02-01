from collections import defaultdict


class Solution:

    def lengthOfLongestSubstringTwoDistinctOfficial(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 2
        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == 3:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count, ans, i, j = {}, 0, 0, 0
        prev, secPrev = '*', '*'
        while j < len(s):
            if s[j] in count:
                if s[j] == prev and secPrev != '*':
                    prev, secPrev = secPrev, prev
            elif len(count) == 2 and s[j] not in count:
                i = count[prev]
                i += 1
                del count[prev]
                prev = secPrev
                secPrev = s[j]
            elif len(count) == 1:
                secPrev = s[j]
            else:
                prev = s[j]
            count[s[j]] = j
            ans = max(ans, j - i + 1)
            j += 1
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinctOfficial("ccaabbb"))

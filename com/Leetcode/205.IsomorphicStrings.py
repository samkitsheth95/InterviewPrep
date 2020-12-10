class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d, used = {}, set()
        i, n = 0, len(s)
        while i < n:
            if s[i] in d:
                if t[i] != d[s[i]]:
                    return False
            else:
                if t[i] not in used:
                    d[s[i]] = t[i]
                    used.add(t[i])
                else:
                    return False
            i += 1
        return True

    def isIsomorphicMap(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]


sol = Solution()
print(sol.isIsomorphicMap(s="egg", t="add"))

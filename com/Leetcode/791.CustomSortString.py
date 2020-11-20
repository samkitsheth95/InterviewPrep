from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c = Counter(T)
        ans = ''
        for i in S:
            ans += i * c[i]
            c[i] = 0
        for key, value in c.items():
            ans += key * value
        return ans

    def customSortStringNaive(self, S: str, T: str) -> str:
        order = {}
        lenS, lenT = len(S), len(T)
        st = 1
        for i in range(lenS):
            order[S[i]] = st
            st += 1
        for i in range(26):
            if chr(ord('a') + i) not in order:
                order[chr(ord('a') + i)] = st
                st += 1
        custC = []
        for i in T:
            custC.append(order[i])
        custC.sort()
        ans = ''
        res = dict((v, k) for k, v in order.items())
        for i in custC:
            ans += res[i]
        return ans


sol = Solution()
print(sol.customSortString(S="cba", T="abcd"))

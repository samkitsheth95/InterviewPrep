from collections import deque


class Solution:
    def minKBitFlips(self, A, K) -> 'int':
        q = deque()
        res = 0
        for i in range(len(A)):
            if len(q) % 2 != 0:
                if A[i]:
                    res += 1
                    q.append(i+K-1)
            else:
                if not A[i]:
                    res += 1
                    q.append(i+K-1)
            if q and q[0] == i:
                q.popleft()
            if q and q[-1] >= len(A):
                return -1
        return res


sol = Solution()
print(sol.minKBitFlips(A=[0, 1, 0], K=1))

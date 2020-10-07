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

    def minKBitFlips1(self, A: 'List[int]', K: 'int') -> 'int':
        flip = 0
        const = 10
        res = 0
        for i in range(len(A)):
            if flip % 2 != 0:
                if A[i] % 10:
                    res += 1
                    flip += 1
                    if i + K - 1 >= len(A):
                        return -1
                    A[i + K - 1] += const
            else:
                if not A[i] % 10:
                    res += 1
                    flip += 1
                    if i + K - 1 >= len(A):
                        return -1
                    A[i + K - 1] += const
            if A[i] > 1:
                flip -= 1
        return res


sol = Solution()
print(sol.minKBitFlips1(A=[0, 1, 0], K=1))

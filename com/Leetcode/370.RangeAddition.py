from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        for i, j, k in updates:
            ans[i] += k
            ans[j + 1] -= k
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        ans.pop()
        return ans

    def getModifiedArrayNaive(self, length: int, updates: List[List[int]]) -> List[int]:
        data = [[0] * 2 for _ in range(length)]
        for i, j, k in updates:
            data[i][0] += k
            data[j][1] += k
        ans, x, idx = [], 0, 0
        for i, j in data:
            idx += data[x][0]
            ans.append(idx)
            idx -= data[x][1]
            x += 1
        return ans


sol = Solution()
print(sol.getModifiedArray(
    length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]))

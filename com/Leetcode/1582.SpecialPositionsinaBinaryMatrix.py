from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = [0] * len(mat)
        col = [0] * len(mat[0])
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    row[i] += 1
                    col[j] += 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans


sol = Solution()
print(sol.numSpecial(mat=[[0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 1]]))

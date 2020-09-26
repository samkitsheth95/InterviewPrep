from typing import List


class Solution:
    def createRow(self, first, second):
        x = []
        x.append(first[0]+second[0])
        for i in range(len(second)-2):
            x.append(min(first[i]+second[i+1], first[i+1]+second[i+1]))
        x.append(first[len(first)-1]+second[len(second)-1])
        return x

    def minimumTotalTopDown(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        row = self.createRow(triangle[0], triangle[1])
        for i in range(2, len(triangle)):
            row = self.createRow(row, triangle[i])
        return min(row)

    def minimumTotalBottomUp(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(
                    triangle[i][j]+triangle[i+1][j], triangle[i][j]+triangle[i+1][j+1])
        return triangle[0][0]


sol = Solution()
print(sol.minimumTotalBottomUp([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

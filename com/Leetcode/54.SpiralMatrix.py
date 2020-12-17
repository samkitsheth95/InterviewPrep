from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rs, re = 0, len(matrix) - 1
        cs, ce = 0, len(matrix[0]) - 1
        ans = []
        while cs <= ce and rs <= re:
            for i in range(cs, ce + 1):
                ans.append(matrix[rs][i])
            for i in range(rs + 1, re + 1):
                ans.append(matrix[i][ce])
            # if rows are same don't go again, rs alredy done
            if rs != re:
                for i in range(ce - 1, cs - 1, -1):
                    ans.append(matrix[re][i])
            # if cols are same don't go again, cs alredy done
            if cs != ce:
                for i in range(re - 1, rs, -1):
                    ans.append(matrix[i][cs])
            cs += 1
            ce -= 1
            rs += 1
            re -= 1
        return ans




sol = Solution()
print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

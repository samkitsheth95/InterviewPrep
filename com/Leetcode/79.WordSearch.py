from typing import List


class Solution:

    def dfs(self, board, word, i, j, k, row, col):
        if k == len(word):
            return True
        if i >= row or i < 0 or j >= col or j < 0 or board[i][j] != word[k]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        k += 1
        res = self.dfs(board, word, i - 1, j, k, row, col) or self.dfs(board, word, i + 1, j, k, row,
                                                                       col) or self.dfs(board, word, i, j - 1, k, row, col) or self.dfs(board, word, i, j + 1, k, row, col)
        board[i][j] = tmp
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j]:
                    if self.dfs(board, word, i, j, 0, row, col):
                        return True
        return False


sol = Solution()
print(sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], [
      "A", "D", "E", "E"]], word="ABCESEEEFS"))

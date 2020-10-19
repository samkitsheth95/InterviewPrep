class Solution(object):
    def didWin(self, board, x):
        find = x*3
        for i in board:
            if find in i:
                return True
        t = ""
        for i in range(3):
            t = ""
            for j in range(3):
                t += board[j][i]
            if find in t:
                return True
        q = ""
        for i in range(3):
            q += board[i][i]
        if find in q:
            return True
        q = ""
        j = 0
        for i in range(2, -1, -1):
            q += board[j][i]
            j += 1
        if find in q:
            return True
        return False

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        status = ''.join(board)
        oc = status.count("O")
        xc = status.count("X")
        if oc > xc:
            return False
        if xc > oc + 1:
            return False
        if self.didWin(board, "X") and oc == xc:
            return False
        if self.didWin(board, "O") and oc < xc:
            return False
        if self.didWin(board, "O") and self.didWin(board, "X"):
            return False
        return True


sol = Solution()
print(sol.validTicTacToe(board=["XOX", "O O", "XOX"]))

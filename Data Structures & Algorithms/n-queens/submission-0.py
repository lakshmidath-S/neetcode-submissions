class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board, row, col, n):
            for i in range(row):
                if board[i] == col:
                    return False
                if abs(i - row) == abs(board[i] - col):
                    return False
            return True
        def ak(board, row, n, ans):
            if row == n:
                solution = []
                for col in board:
                    s = "." * col + "Q" + "." * (n - col - 1)
                    solution.append(s)
                ans.append(solution)
                return
            for col in range(n):
                if isSafe(board, row, col, n):
                    board[row] = col
                    ak(board, row + 1, n, ans)
                    board[row] = -1
        board = [-1] * n
        ans = []
        ak(board, 0, n, ans)
        return ans

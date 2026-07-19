class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=len(board[0])
        row=len(board)
        for i in range(col):
            cols=set()
            for j in range(row):
                if board[j][i]!='.':
                    if board[j][i] in cols:
                        return False 
                    else: 
                        cols.add(board[j][i])
        for i in range(row):
            rows=set()
            for j in range(col):
                if board[i][j]!='.':
                    if board[i][j] in rows:
                        return False 
                    else:
                        rows.add(board[i][j])
        for n in range(3):
            for k in range(3):
                grid=set()
                for i in range(3*n,3*(n+1)):
                    for j in range(3*k,3*(k+1)):
                        if board[i][j]!='.':
                            if board[i][j] in grid:
                                return False 
                            else:
                                grid.add(board[i][j])
        return True

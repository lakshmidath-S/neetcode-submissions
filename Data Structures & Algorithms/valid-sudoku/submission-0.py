class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        col=len(board[0])
        row=len(board)
        for i in range(col):
            for j in range(row):
                if board[j][i]!='.':
                    cols[i].append(board[j][i])

        for i in range(col):
            if len(cols[i])!=len(set(cols[i])):
                return False

        for i in range(row):
            for j in range(col):
                if board[i][j]!='.':
                    rows[i].append(board[i][j])

        for i in range(row):
            if len(rows[i])!=len(set(rows[i])):
                return False

        grid = [[] for _ in range(9)]
        i,j=0,0
        m=0
        n=0
        k=0
        o=0
        for n in range(3):
            for k in range(3):
                for i in range(3*n,3*(n+1)):
                    for j in range(3*k,3*(k+1)):
                        if board[i][j]!='.':
                            grid[o].append(board[i][j])
                o+=1
        for i in range(9):
            if len(grid[i])!=len(set(grid[i])):
                return False
        return True

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        col=len(board[0])
        visited=[[False]* col for _ in range(row)]
        changed=[[False]* col for _ in range(row)]
        def isSurrounded(i,j):
            flag=True
            if i<0 or j<0 or i>=row or j>=col:
                return flag
            if visited[i][j] or board[i][j]=='X':
                return flag
            visited[i][j]=True
            if i==0 or j==0 or i==row-1 or j==col-1:
                flag=False
            return (flag & isSurrounded(i,j+1) & isSurrounded(i,j-1) & isSurrounded(i+1,j) & isSurrounded(i-1,j))

        def change(i,j):
            if i<0 or j<0 or i>=row or j>=col:
                return
            if changed[i][j] or board[i][j]=='X':
                return 
            changed[i][j]=True
            board[i][j]='X'
            change(i,j+1)
            change(i,j-1)
            change(i+1,j)
            change(i-1,j)
            
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and not visited[i][j]:
                    if isSurrounded(i,j):
                        change(i,j)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        n=len(word)
        visited=[[False]*c for _ in range(r)]
        def dfs(i,j,k):
            if i>=r or j>=c or k>n or i<0 or j<0:
                return False
            if visited[i][j]:
                return False
            if board[i][j]!=word[k]:
                return False
            if k==n-1:
                return True
            visited[i][j]=True
            found=(dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
            visited[i][j]=False
            return found
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False